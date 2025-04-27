
import pandas as pd



def extract_data(file_path: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return pd.DataFrame()



def transform_data(data: pd.DataFrame) -> pd.DataFrame:

    data.drop(data.iloc[:, 2:44], inplace=True, axis=1)

   
    data_clean = data.dropna()

    
    data_column = data_clean.columns[-1]
    data_clean[data_column] = data_clean[data_column].astype(float).round(2)

    return data_clean




import argparse
import psycopg2
from extract import extract_data
from transform import transform_data


def load_data(file_path: str):
    
    conn = psycopg2.connect(
        dbname="energy_consumption",
        user="postgres",
        password="123456",
        host="localhost",
        port="5434"
    )
    cur = conn.cursor()

    print("Loading data...")
    df = extract_data(file_path)

    print("Transforming data...")
    transformed = transform_data(df)

    
    table = transformed.columns[-1].lower()

    
    create_sql = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        id SERIAL PRIMARY KEY,
        continent VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        {table} DECIMAL
    );
    """
    cur.execute(create_sql)

    
    insert_sql = f"INSERT INTO {table} (continent, country, {table}) VALUES (%s, %s, %s);"
    for _, row in transformed.iterrows():
        cur.execute(insert_sql, (row['Continent'], row['Country'], row[transformed.columns[-1]]))

    conn.commit()
    cur.close()
    conn.close()

    print("ETL success...\n")


def main():
    
    default_path = "/app/data/Energy Statistics/Consumption_Data/Consumption_Coal.csv"
    file_path = sys.argv[1] if len(sys.argv) > 1 else default_path
    
    
    load_data(file_path)

if __name__ == "__main__":
    main()