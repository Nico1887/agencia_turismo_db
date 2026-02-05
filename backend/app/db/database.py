import pyodbc

import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Trabajo_Practico_Agencia_De_Viajes;"
        "Trusted_Connection=yes;"
    )
    return conn


