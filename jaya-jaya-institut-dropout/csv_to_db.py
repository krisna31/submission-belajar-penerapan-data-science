from sqlalchemy import create_engine
import pandas as pd

URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(URL)
pd.read_csv("student_data.csv", sep=';').to_sql('students', engine)