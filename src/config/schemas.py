# src/config/schemas.py
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, BooleanType

# --- Bronze Layer Schemas ---

customer_schema = StructType([
    StructField("member_id", StringType(), True),
    StructField("emp_title", StringType(), True),
    StructField("emp_length", StringType(), True),
    StructField("home_ownership", StringType(), True),
    StructField("annual_inc", FloatType(), True),
    StructField("addr_state", StringType(), True),
    StructField("zip_code", StringType(), True),
    StructField("country", StringType(), True),
    StructField("grade", StringType(), True),
    StructField("sub_grade", StringType(), True),
    StructField("verification_status", StringType(), True),
    StructField("tot_hi_cred_lim", FloatType(), True),
    StructField("application_type", StringType(), True),
    StructField("annual_inc_joint", FloatType(), True),
    StructField("verification_status_joint", StringType(), True),
    StructField("_rescued_data", StringType(), True)
])

defaulters_schema = StructType([
    StructField("member_id", StringType(), True),
    StructField("delinq_2yrs", FloatType(), True),
    StructField("delinq_amnt", FloatType(), True),
    StructField("pub_rec", FloatType(), True),
    StructField("pub_rec_bankruptcies", FloatType(), True),
    StructField("inq_last_6mths", FloatType(), True),
    StructField("total_rec_late_fee", FloatType(), True),
    StructField("mths_since_last_delinq", FloatType(), True),
    StructField("mths_since_last_record", FloatType(), True),
    StructField("_rescued_data", StringType(), True)
])

loans_schema = StructType([
    StructField("loan_id", StringType(), True),
    StructField("member_id", StringType(), True),
    StructField("loan_amnt", FloatType(), True),
    StructField("funded_amnt", FloatType(), True),
    StructField("term", StringType(), True),
    StructField("int_rate", FloatType(), True),
    StructField("installment", FloatType(), True),
    StructField("issue_d", StringType(), True),
    StructField("loan_status", StringType(), True),
    StructField("purpose", StringType(), True),
    StructField("title", StringType(), True),
    StructField("_rescued_data", StringType(), True)
])

repayments_schema = StructType([
    StructField("loan_id", StringType(), True),
    StructField("total_rec_prncp", FloatType(), True),
    StructField("total_rec_int", FloatType(), True),
    StructField("total_rec_late_fee", FloatType(), True),
    StructField("total_pymnt", FloatType(), True),
    StructField("last_pymnt_amnt", FloatType(), True),
    StructField("last_pymnt_d", StringType(), True),
    StructField("next_pymnt_d", StringType(), True),
    StructField("_rescued_data", StringType(), True)
])

# --- Silver/Lookup Table Schemas ---

POINTS_MAPPING_SCHEMA = StructType([
    StructField("rating_id", IntegerType(), False),
    StructField("rating_key", StringType(), False),
    StructField("points", IntegerType(), False)
])

LOAN_PURPOSES_SCHEMA = StructType([
    StructField("loan_purpose", StringType(), False),
    StructField("is_active", BooleanType(), False)
])

GRADING_SCALE_SCHEMA = StructType([
    StructField("grade_id", IntegerType(), False),
    StructField("grade_name", StringType(), False),
    StructField("min_score", IntegerType(), False),
    StructField("max_score", IntegerType(), False),
    StructField("description", StringType(), True)
])