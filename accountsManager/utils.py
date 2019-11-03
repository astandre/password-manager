import re


def verify_password(password):
    return re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)
