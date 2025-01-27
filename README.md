# Complex SQL Query for a MySQL Database



***

#### Purpose

This repo includes a Python script to interact with an SQL Database on Azure Databricks. The project also implements continuous integration through GitHub Actions to automate the setup of the environment, perform testing, code formatting, and code linting.

***

#### ETL-Query Operations

Extract (E): Retrieves a dataset in CSV format from a specified URL.
Transform (T): Cleans, filters, and enriches the extracted data, preparing it for analysis.
Load (L): Loads the transformed data into a SQLite Database table using Python's sqlite3 module.
Query (Q): Writes and executes SQL queries on the SQLite database to analyze and extract insights from the data.

****

Dataset: [Baskin Robbins Ice-Cream](https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/baskin_icecream.csv)

***

### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```
5. ```
   # To extract data
   make extract
   ```
6. ```
   # To tranform data
   make transform_load
   ```
7. ```
   # To query data
   make query
   ```
