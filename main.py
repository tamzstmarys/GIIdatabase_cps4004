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

cursor.execute("""
INSERT INTO Claim (policy_id, date, type, status, description)
VALUES (?, '2025-04-01', 'Accident', 'Rear end collision on the highway.'
""", (policy_id,))
claim_id = cursor.lastrowid
