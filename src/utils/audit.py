# src/utils/audit.py
import uuid
from pyspark.sql.functions import current_timestamp, col, lit

def get_batch_id(job_run_id: str) -> str:
    """
    Evaluates the Job Run ID passed from the orchestrator.
    If the run is manual (empty), generates a unique UUID for traceability.
    """
    if not job_run_id:
        # Appends a UUID slice to ensure manual runs have a unique, traceable ID
        return f"manual_run_{uuid.uuid4().hex[:8]}"
    
    return job_run_id

def add_bronze_metadata(df):
    """
    Standardized lineage for Bronze (Unity Catalog Compliant).
    Extracts file path from the UC-native _metadata struct.
    """
    return df.withColumn("_ingested_at", current_timestamp()).withColumn(
        "_source_file", col("_metadata.file_path")
    ) 

def apply_silver_metadata(df):
    """
    Injects Silver update timestamps and purges transient Bronze/CDF metadata.
    """
    transient_cols = [
        "_commit_version",
        "_commit_timestamp",
        "_rescued_data"
    ]

    # Preserve the Bronze commit version for Silver lineage fencing
    if "_commit_version" in df.columns:
        df = df.withColumn("_bronze_version", col("_commit_version"))

    # Append execution timestamp and purge transient columns
    return df.withColumn("_updated_at", current_timestamp()).drop(*transient_cols)

def add_ref_metadata(df):
    """
    Standardizes technical metadata for reference (lookup) tables.
    """
    return (df
        .withColumn("_updated_at", current_timestamp())        
        .withColumn("_source_file", col("_metadata.file_path"))
        .withColumn("_processed_by", lit("lending_risk_ingest_job"))
    )

def apply_gold_metadata(df, module_name):
    """
    Applies business-level lineage for Gold scoring tables.
    """
    return (df
        .withColumn("_updated_at", current_timestamp())
        .withColumn("_scoring_module", lit(module_name))
    )