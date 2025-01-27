import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Create Schedules table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Schedules (
    DoctorName TEXT PRIMARY KEY,
    Monday TEXT,
    Tuesday TEXT,
    Wednesday TEXT,
    Thursday TEXT,
    Friday TEXT,
    Saturday TEXT,
    Sunday TEXT
)
''')

# Insert data from Excel sheet
def insert_data_from_excel():
    excel_file = 'data/Xyris HIS_data.xlsx'
    df = pd.read_excel(excel_file, sheet_name='Schedules')
    df.to_sql('Schedules', conn, if_exists='replace', index=False)

# Run the data insertion
insert_data_from_excel()

# Commit changes and close connection
conn.commit()
conn.close()