import mysql.connector as mc
from cryptography.fernet import Fernet


def keyyer(path):
    try:
        with open(path) as key:
            key = key.read()
        return key
    except Exception as e:
        print(e)


def password_update_username(username, path):
    mydb = mc.connect(host="localhost", user='root', password='1234', database='password') 
    conn = mydb.cursor()

    try:

        key = keyyer(path)
        f = Fernet(key)
        conn.execute(f"select * from manager where Username='{username}'")
        res = conn.fetchall()
        for row in res:
            print(f"Sl.No: {row[0]}")
            print(f"Website/App: {row[1]}")
            print(f"Username: {row[2]}")
            print(f"Password: {(f.decrypt(bytes(row[3],'utf-8'))).decode()}")
    except Exception as e:
        print(e)

    sl = int(input("Enter Sl.No of the Website/Address you want to update: "))
    new_pass = input("Enter new password: ")
    en_pass = f.encrypt(bytes(new_pass,'utf-8'))

    try:
        conn.execute(f"update manager set passy='{en_pass.decode()}' where Sl_No={sl}")
        mydb.commit()
        return "Done"
    except Exception as e:
        return e


def password_update_name(website, path):
    mydb = mc.connect(host="localhost", user='root', password='1234', database='password')
    conn = mydb.cursor()

    try:
        key=keyyer(path)
        f=Fernet(key)
        conn.execute(f"select * from manager where Website_App='{website}'")
        res = conn.fetchall()
        for row in res:
            print(f"Sl.No: {row[0]}")
            print(f"Website/App: {row[1]}")
            print(f"Username: {row[2]}")
            print(f"Password: {(f.decrypt(bytes(row[3],'utf-8'))).decode()}")

    except Exception as e:
        print(e)

    sl = int(input("Enter Sl.No of the Website/Address you want to update: "))

    new_pass = input("Enter new password: ")
    en_pass = f.encrypt(bytes(new_pass,'utf-8'))
    print(en_pass)


    try:
        conn.execute(f"update manager set passy='{en_pass.decode()}' where Sl_No={sl}")
        return "Done"
    except Exception as e:
        return e
