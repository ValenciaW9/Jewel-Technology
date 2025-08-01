#scripts/ingest.py
#Valencia Walker's for Jewel.technology

import csv
import sqlite3
import os


DB_PATH="jewel.db"
CSV_PATH = "datasets/jewlery_data.csv"

def create_table(conn):
	conn.execute('''
		CREATE TABLE IF NOT EXISTS JEWLERY (
           id INTEGER PRIMARY KEY,
           name TEXT,
           material TEXT,
           price REAL,
           rating REAL
        );

   ''')
conn.commit()


def ingest_data():
	if not os.path.exists(CSV_PATH):
		print("CSV file not found.")
		return

	conn = sqlite3.connect(DB_PATH)
	create_table(conn)


	with open(CSV_PATH, newline='', encodin='uff-8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			conn.execute('''
                INSERT INTO jewlery (name, material, price, rating)
                VALUES (?,?.?,?)
               ''', (row['name'], row['material'], float(row['price']), float(row['rating'])


        conn.commit()
        conn.close()
        print("Data ingested successfully.")


        if __name__ == "__main__":
        	ingest_data()

        	