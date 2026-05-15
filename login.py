users = {
    "admin": "1234",
    "arti": "pass",
    "user": "user123"
}

def authenticate(username, password):

    if username in users:

        if users[username] == password:

            return True

    return False