# src/config/paths.py

class ProjectConfig:
    """
    Centralized configuration for the Lending Risk Framework.
    Instantiated with environment-specific parameters passed from the DAB.
    """
    def __init__(self, catalog: str, raw_path: str):
        if not catalog:
            raise ValueError("CATALOG parameter is empty. Check DAB base_parameters mapping.")
        if not raw_path:
            raise ValueError("RAW_PATH parameter is empty. Check DAB base_parameters mapping.")

        # --- Core Parameters ---
        self.CATALOG = catalog
        self.RAW_PATH = raw_path

        # --- Schemas ---
        self.SCHEMAS = ["raw", "bronze", "silver", "gold"]
        self.RAW_SCHEMA = f"{self.CATALOG}.raw" 
        self.BRONZE_SCHEMA = f"{self.CATALOG}.bronze"
        self.SILVER_SCHEMA = f"{self.CATALOG}.silver"
        self.GOLD_SCHEMA = f"{self.CATALOG}.gold"

        # --- Bronze Table Paths (3-Level Namespace) ---
        self.CUSTOMERS_BRONZE = f"{self.BRONZE_SCHEMA}.customers"
        self.LOANS_BRONZE = f"{self.BRONZE_SCHEMA}.loans"
        self.DEFAULTERS_BRONZE = f"{self.BRONZE_SCHEMA}.defaulters"
        self.REPAYMENTS_BRONZE = f"{self.BRONZE_SCHEMA}.repayments"

        # --- Silver Table Paths (3-Level Namespace) ---
        self.CUSTOMERS_SILVER = f"{self.SILVER_SCHEMA}.customers"
        self.LOANS_SILVER = f"{self.SILVER_SCHEMA}.loans"
        self.DEFAULTERS_INQUIRY_SILVER = f"{self.SILVER_SCHEMA}.defaulters_inquiry"
        self.DEFAULTERS_DELINQ_SILVER = f"{self.SILVER_SCHEMA}.defaulters_delinq"
        self.REPAYMENTS_SILVER = f"{self.SILVER_SCHEMA}.repayments"

        # --- Gold Table Paths (3-Level Namespace) ---
        self.CALC_PAYMENT_PERF_GOLD = f"{self.GOLD_SCHEMA}.calc_payment_performance"

        # --- Reference & Lookup Table Definitions ---
        self.REF_LOAN_PURPOSES = f"{self.SILVER_SCHEMA}.ref_loan_purposes"
        self.REF_SCORE_POINTS = f"{self.SILVER_SCHEMA}.ref_score_points_mapping"
        self.REF_LOAN_GRADING = f"{self.SILVER_SCHEMA}.ref_loan_grading_scale"

        # --- Unity Catalog Volume Path (Raw) ---
        self.RAW_VOLUME = f"/Volumes/{self.CATALOG}/raw/vol_raw"

        # --- Source Data Sub-Directories ---
        self.SRC_CUSTOMERS = f"{self.RAW_VOLUME}/customers/"
        self.SRC_LOANS = f"{self.RAW_VOLUME}/loans/"
        self.SRC_DEFAULTERS = f"{self.RAW_VOLUME}/defaulters/"
        self.SRC_REPAYMENTS = f"{self.RAW_VOLUME}/repayments/"
        
        # --- Reference Data Paths ---
        self.GRADING_SOURCE_PATH = f"{self.RAW_VOLUME}/_references/ref_loan_grading_scale.csv"
        self.LOAN_PURPOSE_PATH = f"{self.RAW_VOLUME}/_references/ref_loan_purpose_lookup.csv"
        self.POINTS_SOURCE_PATH = f"{self.RAW_VOLUME}/_references/ref_score_points_mapping.csv"

        # --- Bronze Checkpoints ---
        self.CHECKPOINT_BASE_BRONZE = f"/Volumes/{self.CATALOG}/bronze/vol_bronze/_checkpoints"
        self.BRONZE_CHECKPOINT_CUSTOMERS = f"{self.CHECKPOINT_BASE_BRONZE}/customers"
        self.BRONZE_CHECKPOINT_LOANS = f"{self.CHECKPOINT_BASE_BRONZE}/loans"
        self.BRONZE_CHECKPOINT_DEFAULTERS = f"{self.CHECKPOINT_BASE_BRONZE}/defaulters"
        self.BRONZE_CHECKPOINT_REPAYMENTS = f"{self.CHECKPOINT_BASE_BRONZE}/repayments"

        # --- Silver Checkpoints ---
        self.CHECKPOINT_BASE_SILVER = f"/Volumes/{self.CATALOG}/silver/vol_silver/_checkpoints"
        self.SILVER_CHECKPOINT_CUSTOMERS = f"{self.CHECKPOINT_BASE_SILVER}/customers"
        self.SILVER_CHECKPOINT_LOANS = f"{self.CHECKPOINT_BASE_SILVER}/loans"
        self.SILVER_CHECKPOINT_DEFAULTERS_DELINQ = f"{self.CHECKPOINT_BASE_SILVER}/defaulters_delinq"
        self.SILVER_CHECKPOINT_DEFAULTERS_INQUIRY = f"{self.CHECKPOINT_BASE_SILVER}/defaulters_inquiry"
        self.SILVER_CHECKPOINT_REPAYMENTS = f"{self.CHECKPOINT_BASE_SILVER}/repayments"

        # --- Gold Checkpoints --- 
        self.CHECKPOINT_BASE_GOLD = f"/Volumes/{self.CATALOG}/gold/vol_gold/_checkpoints"
        self.GOLD_CHECKPOINT_PAYMENT_PERF = f"{self.CHECKPOINT_BASE_GOLD}/payment_performance"
        self.GOLD_CHECKPOINT_DEFAULTERS_PERF = f"{self.CHECKPOINT_BASE_GOLD}/defaulters_performance"
        self.GOLD_CHECKPOINT_FINANCIAL_PERF = f"{self.CHECKPOINT_BASE_GOLD}/financial_performance"