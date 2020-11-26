import mysql.connector as mc
from cryptography.fernet import Fernet

def keyyer(path):
    try:
        with open(path) as key:
            key=key.read()
        return key
    except Exception as e:
        print(e)


def finder_username(username,path):
    mydb=mc.connect(host="localhost", user='root', password='1234',database='password')
    conn=mydb.cursor()

    try:
        key=keyyer(path)
        f=Fernet(key)
        conn.execute(f"select passy,Website_App from manager where Username='{username}'")
        res=conn.fetchall()
        for row in res:
            print("Website/App: ",row[1])
            print("Password: ", (f.decrypt(bytes(row[0],'utf-8'))).decode())
    except Exception as e:
        print(f"ERROR: {e}")

def finder_website(website,path):
    mydb=mc.connect(host="localhost", user='root', password='1234',database='password')
    conn=mydb.cursor()

    try:
        key=keyyer(path)
        f=Fernet(key)
        print("s")
        conn.execute(f"select passy,Username from manager where Website_App='{website}'")
        res=conn.fetchall()
        for row in res:
            print("Username: ",row[1])
            print("Password: ", (f.decrypt(bytes(row[0],'utf-8'))).decode())
    except Exception as e:
        print(e)