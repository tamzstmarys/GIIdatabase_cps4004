import sqlite3

conn=sqlite3.connect("insurance.db")
cursor = conn.cursor()

customer_id = cursor.lastrowid
cursor.execute("""
INSERT INTO Customer (name, telephone, email)
VALUES ('Tahmid Miah', 'tamz@outlook.com', '440252525')
""")

cursor.execute("""
INSERT INTO Policy (customer_id, premium_amount, coverage_details)
VALUES (?, ?, ?)
""", (customer_id, 169.69, 'Comprehensive auto insurance'))
policy_id = cursor.lastrowid
