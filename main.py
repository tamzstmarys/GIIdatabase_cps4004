import sqlite3

conn = sqlite3.connect("insurance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Policy (
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    premium_amount REAL,
    coverage_details TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Claim (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER,
    date TEXT,
    type TEXT,
    status TEXT,
    description TEXT,
    FOREIGN KEY (policy_id) REFERENCES Policy(policy_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Incident (
    incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id INTEGER,
    date TEXT,
    location TEXT,
    report TEXT,
    FOREIGN KEY (claim_id) REFERENCES Claim(claim_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY (claim_id) REFERENCES Claim(claim_id)
)
""")

cursor.execute("""
INSERT INTO Customer (name, phone, email)
VALUES ('Tahmid Miah', '440252525', 'tamz@outlook.com')
""")
customer_id = cursor.lastrowid

cursor.execute("""
INSERT INTO Policy (customer_id, premium_amount, coverage_details)
VALUES (?, ?, ?)
""", (customer_id, 169.69, 'Comprehensive auto insurance'))
policy_id = cursor.lastrowid

cursor.execute("""
INSERT INTO Claim (policy_id, date, type, status, description)
VALUES (?, '04/01/2025', 'Accident', 'Processing', 'Rear end collision on the highway')
""", (policy_id,))
claim_id = cursor.lastrowid

cursor.execute("""
INSERT INTO Incident (claim_id, date, location, report)
VALUES (?, '28/12/2025', 'Kennington', 'Accident occurred at junction, no injuries.')
""", (claim_id,))

cursor.execute("""
INSERT INTO Payment (claim_id, amount, date)
VALUES (?, 120.50, '04/02/2025')
""", (claim_id,))

conn.commit()
conn.close()

print("Your sample data has been entered successfully.")