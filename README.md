# Project Overview
![for project](https://github.com/user-attachments/assets/d03139f3-ecf7-4795-9369-215f63d1a81a)

This project implements a simple ETL (Extract, Transform, Load) process. It uses the following technologies:

-Python programming language

-Docker

-PostgreSQL

-Data directory: Contains all the data downloaded from the Global Energy Statistics - Kaggle dataset

# ETL (Extract, Transform, Load):

## Extract
The extraction step is used to extract data from data sources. Since the dataset only has one format, I use the pandas library to extract data from a CSV file and load it into a DataFrame. Once extracted, the data is returned as a DataFrame.

## Transform

In the transformation step, I use Python to clean and transform the data as needed. Here’s what I do:

  -I remove unnecessary columns. In this case, I only keep the columns [Continent, Country, and the last column of the file].

  -I remove missing values from the dataset using the .dropna() function from pandas.

  -The data type of the last column is float, and it has many digits after the decimal. I round the values so that they only have 2 digits after the decimal point.

  -After transforming the values in the last column, I create a new DataFrame with the transformed column and replace the old column with the new one.

## Load
The loading step is used to load the transformed data into a data warehouse or database. In this case, I use PostgreSQL with a Docker image, which I will explain later in the Docker section. I use psycopg2 to connect Python to PostgreSQL. Additionally, I use argparse to create command-line arguments in Python so I can flexibly input the CSV file, database name, host name, username, password, and port of PostgreSQL.
