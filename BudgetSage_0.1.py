import pandas as pd
import sqlite3
from pathlib import Path

# Paths for the CSV file directory and SQLite database
csv_folder = Path("/data/csv_files")  # Mounted folder with CSV files
db_path = "/data/financial_data.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the transactions table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Bewertungsdatum TEXT,
        Bankbeziehung TEXT,
        Portfolio TEXT,
        Produkt TEXT,
        IBAN TEXT,
        Whrg TEXT,
        Datum_von TEXT,
        Datum_bis TEXT,
        Beschreibung TEXT,
        Abschluss TEXT,
        Buchungsdatum TEXT,
        Valuta TEXT,
        Beschreibung1 TEXT,
        Beschreibung2 TEXT,
        Beschreibung3 TEXT,
        Transaktions_Nr TEXT,
        Devisenkurs REAL,
        Einzelbetrag REAL,
        Belastung REAL,
        Gutschrift REAL,
        Saldo REAL,
        Category TEXT DEFAULT NULL
    )
''')
conn.commit()

def import_csv(file_path):
    # Read CSV into DataFrame
    df = pd.read_csv(file_path, delimiter=';')

    # Convert columns with Swiss numeric format (like "1'000.00") to floats
    for col in ['Einzelbetrag', 'Belastung', 'Gutschrift', 'Saldo']:
        df[col] = df[col].replace("'", "", regex=True).astype(float)

    # Insert each row into the transactions table
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO transactions (
                Bewertungsdatum, Bankbeziehung, Portfolio, Produkt, IBAN, Whrg, Datum_von, Datum_bis,
                Beschreibung, Abschluss, Buchungsdatum, Valuta, Beschreibung1, Beschreibung2,
                Beschreibung3, Transaktions_Nr, Devisenkurs, Einzelbetrag, Belastung, Gutschrift, Saldo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['Bewertungsdatum'], row['Bankbeziehung'], row['Portfolio'], row['Produkt'], row['IBAN'],
            row['Whrg.'], row['Datum von'], row['Datum bis'], row['Beschreibung'], row['Abschluss'],
            row['Buchungsdatum'], row['Valuta'], row['Beschreibung 1'], row['Beschreibung 2'],
            row['Beschreibung 3'], row['Transaktions-Nr.'], row['Devisenkurs zum Originalbetrag in Abrechnungswährung'],
            row['Einzelbetrag'], row['Belastung'], row['Gutschrift'], row['Saldo']
        ))
    conn.commit()
    print(f"Imported {file_path} into the database.")

# Automatically import all CSV files in the specified folder
for csv_file in csv_folder.glob("*.csv"):
    import_csv(csv_file)

conn.close()
