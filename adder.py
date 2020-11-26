import datetime
import mysql.connector as mc
from cryptography.fernet import Fernet
import re
import base64

def keyyer(path):
    try:
        with open(path) as key:
            key=key.read()
        return key
    except Exception as e:
        print(e)


def add_new(path):
    mydb = mc.connect(host="localhost", user='root', password='1234', database='password')
    conn = mydb.cursor()

    try:
        conn.execute("select MAX(`Sl.No`) from manager")
        sl = conn.fetchone()[0]
        sl += 1
    except:
        sl = 1

    name = input("Enter website or app name: ")
    username = input("Enter username of the website of app: ")
    password = input("Enter password: ")
    da = datetime.datetime.now()

    key=keyyer(path)
    f=Fernet(key)

    en_pass = f.encrypt(bytes(password,'utf-8'))
    try:
        conn.execute(f"insert into manager values ({sl},'{name}','{username}','{en_pass.decode()}')")
        mydb.commit()
        print("New password added")
    except Exception as e:
        print(f"ERROR: {e}")
