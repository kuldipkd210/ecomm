import sqlite3
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS products(
                   id TEXT PRIMARY KEY,
                   cost REAL,
                   category TEXT,
                   name TEXT,
                   brand TEXT,
                   retail_price REAL,
                   department TEXT,
                   sku TEXT,
                   distribution_center_id TEXT
               )
               ''')


conn.commit()
conn.close()
print("Database and table Created Successfully.")