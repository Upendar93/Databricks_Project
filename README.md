# Databricks_Project
FMCG Project
# 🚀 FMCG Sales & Market Analysis | Databricks End-to-End Project

## 📖 Overview
This project demonstrates an end-to-end data engineering and analytics solution built on Databricks. It processes raw FMCG sales data using scalable ETL pipelines, transforms it into business-ready datasets, and delivers insights through dashboards and AI-powered querying.

---
## ☁️ AWS S3 Data Source

Data is stored in AWS S3 with a structured folder hierarchy:

- customers/ → Customer data  
- products/ → Product data  
- orders/ → Transaction data  
- gross_price/ → Pricing data  

S3 acts as the **raw data source (Bronze layer)** for ingestion into Databricks, enabling scalable and distributed processing.

---
## 🏗️ Architecture (Medallion Model)
This project follows the **Medallion Architecture**:

- 🟤 **Bronze Layer** → Raw data ingestion  
- ⚪ **Silver Layer** → Data cleaning & transformation  
- 🟡 **Gold Layer** → Aggregated business-level data  

✔ Implemented using **Delta Lake for reliability and performance**

---

## ⚙️ Data Pipeline (ETL Workflow)

The pipeline is orchestrated using **Databricks Jobs & Workflows**:

- `dim_customers` → Customer data processing  
- `dim_products` → Product data processing  
- `dim_prices` → Pricing data processing  
- `fact_orders` → Final fact table for analytics  

### 🔄 Key Features:
- Incremental data loading  
- Modular pipeline design  
- Optimized transformations using PySpark  

---

## 📊 Dashboard – Sales Insights

An interactive dashboard was built to visualize business performance.

### 🔑 Key Metrics:
- 💰 Total Revenue: **119.93B**
- 📦 Total Quantity Sold: **39.05M**
- 👥 Unique Customers: **54**
- 💵 Average Selling Price: **4052.46**

### 📈 Visualizations:
- Top 10 Products by Revenue  
- Revenue Share by Channel  
- Monthly Revenue Trend  
- Top Variants by Revenue  
- Customer Revenue Analysis  

---

## 🤖 AI-Powered Analytics (Databricks Genie)

This project integrates **Databricks Genie**, enabling users to query data using natural language.

### 🔍 Features:
- Ask questions in plain English  
- Automatically generates SQL queries  
- Enables self-service analytics  

### 💡 Example Queries:
- "What is the monthly revenue trend?"  
- "What is the distribution of orders by market?"  
- "Show top products by revenue"  

### 🚀 Impact:
- Eliminates dependency on SQL for business users  
- Speeds up decision-making  
- Makes data accessible to non-technical stakeholders  

---

## 📈 Key Insights
- Retail channel contributes ~78% of total revenue  
- Revenue significantly increases from September to December  
- Top-performing products and variants identified  
- Customer-level insights support targeted business strategies  

---

## 🛠️ Tech Stack
- Databricks  
- Apache Spark (PySpark)  
- SQL  
- Delta Lake  
- Databricks Workflows  
- Databricks Genie (AI)  
- Data Modeling (Fact & Dimension Tables)  

---

## 📂 Repository Structure
