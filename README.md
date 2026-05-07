# Lending Risk Framework: Azure Databricks (ADLS Gen2)

### Medallion Architecture | Azure Databricks | Unity Catalog | Auto Loader | CDF | Spark Structured Streaming - Batch | DABs - GithubAction

This project implements a production-grade data engineering pipeline using the **Medallion Architecture**. It automates the transformation of raw customer data into actionable loan risk scores and grades using **Azure Databricks** and **Unity Catalog**.

---

## 🛠️ Tech Stack

* **Platform:** Databricks (Unity Catalog).
* **Storage:** Azure Data Lake Storage (ADLS) Gen2.
* **Environment:** PySpark, SQL, Python.
* **Ingestion & Processing:** Auto Loader & Spark Structured Streaming (Batch mode) with Change Data Feed (CDF).
* **CI/CD:** Databricks Asset Bundles (DABs) & GitHub Actions for Dev and Prod workspaces.
* **Orchestration:** Databricks Lakeflow Jobs executed via Service Principal.
* **Visualization:** Power BI.

---

## 🏗️ Data Architecture (Medallion)

The pipeline follows an idempotent, multi-layer transformation logic to ensure data consistency and reliability:

### **Bronze Layer (Raw Ingestion)**

* **Incremental:** Uses **Auto Loader** for efficient raw ingestion from ADLS Gen2.
* **Idempotent:** Design ensures no duplicate data on retries.
* **Governance:** Implemented as managed tables within Unity Catalog.

### **Silver Layer (Cleansed & Conformed)**

* **Incremental:** Utilizes Spark Streaming (Batch) with checkpoints and **Change Data Feed (CDF)**.
* **Logic:** Cleanses and conforms data using Merge/Upsert operations.
* **Enrichment:** Employs broadcast joins with full-load lookup reference tables.
* **Governance:** Managed tables in Unity Catalog.

### **Gold Layer (Analytical & Scoring)**

* **Base Tables:** Flat performance calculations on categories -- defaulter history, financial health, and repayment history using incremental Merge/Upsert logic.
* **Final Risk Score:** A business-ready view built on base tables to calculate risk scores and assign grades (e.g., Excellent, Very Good, Good, Bad, Very Bad).
* **Governance:** Managed tables in Unity Catalog with reference table joins.

---

## 📂 Project Structure

As illustrated in the repository:

* **`src/config/`**: Contains `paths.py` and `schemas.py` for metadata and configuration management.
* **`src/notebooks/`**: Organized by Medallion stage: `01_bronze`, `02_silver`, and `03_gold`.
* **`src/utils/`**: Shared utility modules including `audit.py`, `data_quality.py`, `spark_io.py`, and `transformations.py`.
* **`databricks.yml`**: Configuration for Databricks Asset Bundle deployments.
* **`assets/`**: Contains tables lineage graph and power BI report images.
* **`fixtures/`**: Contains project-specific setup or static data files.

---

## 🛡️ Security & Governance

This project adheres to strict production security standards via Unity Catalog:

* **Service Principal (SP):** Production jobs are run via a dedicated Service Principal to ensure isolation.
* **Least Privilege:** The SP is granted specific `READ FILES` and `MANAGE` permissions only on required External Locations.
* **External Locations:** Raw file access is managed through Unity Catalog External Locations and Storage Credentials.
* **Auditability:** Infrastructure setup is performed by an admin, while operational tasks are restricted to the Service Principal.

---

## 📊 Visuals & Reporting (assets)

* **Lineage:** End-to-end data lineage is tracked within the Databricks Catalog Explorer.
* **Power BI:** Visual reports are generated from the Gold layer to provide executive insights into loan risk distribution.
