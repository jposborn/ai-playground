import pandas as pd
from sqlalchemy import create_engine

db_config = {
    'dbname': 'app_db',
    'user': 'pgadmin',
    'password': 'pgpass',
    'host': 'localhost',
    'port': 5432
}

# Create a SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
)

# Load your CSV file into a DataFrame
csv_file_path = 'data/titanic.csv'
df = pd.read_csv(csv_file_path)

# Write the dataframe to the PostgreSQL table
# Replace 'your_table' with your target table name
df.to_sql('titanic', engine, if_exists='replace', index=False)

print("Data loaded successfully!")
