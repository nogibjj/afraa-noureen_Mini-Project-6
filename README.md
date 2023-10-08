# IDS_706-Data_Engineering_Systems
## Mini-Project 5 : Python Script interacting with SQL Database



***

#### Purpose

This project is for a data engineering course (Mini-Project 5). It involves the use of a Python script to interact with an SQL database. The project also implements continuous integration through GitHub Actions to automate the setup of the environment, perform testing, code formatting, and code linting.

***

#### ETL-Query Operations

Extract (E): Retrieves a dataset in CSV format from a specified URL.
Transform (T): Cleans, filters, and enriches the extracted data, preparing it for analysis.
Load (L): Loads the transformed data into a SQLite Database table using Python's sqlite3 module.
Query (Q): Writes and executes SQL queries on the SQLite database to analyze and extract insights from the data.

****

#### Process

The template given by Professor Noah was used in this project. It was modified by replacing the original dataset (food market) with a dataset related to ice-cream flavours sold by Baskin Robbins. This dataset was extracted into a local CSV file. It was cleaned and transformed, and then loaded into a .db file. SQL queries were then executed to analyze the data. This repo also includes functions for data extraction, transformation and data loading. It also includes a function which implements an SQL log to record all actions performed during queries.

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
***

#### Successful Formatting, Linting and Testing

On running make format, make lint, and make test in actions, it executes succesfully.

![make lint format](https://github.com/nogibjj/afraa-n_Mini-Project-5/assets/143756865/3d2317bf-4aa3-43a5-9b2b-6944022fd48a)
![make test](https://github.com/nogibjj/afraa-n_Mini-Project-5/assets/143756865/7c2b932a-a38d-45d4-8bf6-acd0e312df61)

