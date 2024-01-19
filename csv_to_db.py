from sqlalchemy import create_engine
import pandas as pd

URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(URL)
pd.read_csv("employee_data.csv").to_sql('employee', engine)