import mysql.connector as mc
from cryptography.fernet import Fernet

def keyyer(path):
    try:
        with open(path) as key:
            key = key.read()
        return key
    except Exception as e:
        print(e)

def display(path):
    mydb = mc.connect(host="localhost", user='root', password='1234', database='password')
    conn = mydb.cursor()

    try:

        key = keyyer(path)
        f = Fernet(key)
        conn.execute(f"select * from manager")
        res = conn.fetchall()
        for row in res:
            print(f"Sl.No: {row[0]}")
            print(f"Website/App: {row[1]}")
            print(f"Username: {row[2]}")
            print(f"Password: {(f.decrypt(bytes(row[3],'utf-8'))).decode()}")
    except Exception as e:
        print(e)