from cryptography.fernet import Fernet

def genwrite_key():
    key=Fernet.generate_key()
    with open ("pass.key",'wb') as key_file:
        key_file.write(key)
        key_file.close()

