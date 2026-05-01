# src/utils/spark_io.py

def read_autoloader(spark, source_path, schema, file_format="csv"):
    """
    Standardized Bronze read stream.  
    """
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", file_format)
        .option("header", "true")
        .option("cloudFiles.schemaEvolutionMode", "rescue")
        .schema(schema)
        .load(source_path)
    )

def write_append_stream(df, target_table, checkpoint_loc):
    """
    Standardized Bronze append.
    Ensures exactly-once semantics via checkpoints.
    """
    return (
        df.writeStream.format("delta")
        .outputMode("append")
        .option("checkpointLocation", checkpoint_loc)
        .trigger(availableNow=True)
        .toTable(target_table)
    )

def read_reference_source(spark, source_path, schema):
    """
    Read reference CSV files using standard Spark batch read.
    """
    return (spark.read
            .format("csv")
            .option("header", "true")
            .schema(schema)
            .load(source_path))

def write_reference_table(df, target_table):
    """
    Standardized write for reference/lookup tables.
    Pattern: Atomic Overwrite -> Schema Evolution -> Metadata Refresh.
    """
    (df.write
       .format("delta")
       .mode("overwrite")
       .option("overwriteSchema", "true")
       .saveAsTable(target_table))

def read_delta_stream(spark, table_name, options=None):
    """
    Standardized ReadStream for Delta tables with CDF and Backpressure.
    
    """
    # Production-grade defaults
    default_options = {
        "readChangeFeed": "true",
        "startingVersion": 1,
        "maxFilesPerTrigger": 100  # Backpressure: prevents OOM on initial load
    }
    
    # Merge overrides from the notebook
    if options:
        default_options.update(options)
        
    return (spark.readStream
            .format("delta")
            .options(**default_options)
            .table(table_name))