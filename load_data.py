import pandas as pd
import sqlite3

csv_path = "E:/000/ecomm/archive/products.csv"

df = pd.read_csv(csv_path)
conn = sqlite3.connect("ecommerce.db")

df.to_sql("products",conn,if_exists="replace",index=False)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM products")
print("Record Inserted : ",cursor.fetchone()[0])

conn.close()