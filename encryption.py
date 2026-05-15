from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

cipher = Fernet(key)

# Encrypt Message
def encrypt_message(message):

    return cipher.encrypt(message.encode())

# Decrypt Message
def decrypt_message(message):

    return cipher.decrypt(message).decode()