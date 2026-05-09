import sqlite3
def create_db():
    con = sqlite3.connect(database=r'ims.db')
    con.execute("PRAGMA foreign_keys = ON")

    con.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    
    con.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    con.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    con.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text, FOREIGN KEY (Category) REFERENCES category(name) ON DELETE CASCADE)")
    con.commit()
create_db()
