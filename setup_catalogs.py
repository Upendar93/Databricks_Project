# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS fmcg;
# MAGIC USE CATALOG fmcg;

# COMMAND ----------

# DBTITLE 1,Create gold, silver, bronze schemas
spark.sql("CREATE SCHEMA IF NOT EXISTS fmcg.gold")
spark.sql("CREATE SCHEMA IF NOT EXISTS fmcg.silver")
spark.sql("CREATE SCHEMA IF NOT EXISTS fmcg.bronze")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from fmcg.gold.fact_orders;

# COMMAND ----------

