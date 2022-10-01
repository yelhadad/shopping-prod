import json

import bcrypt, jwt, datetime


def Merge(dict1, dict2):
    res = dict1 | dict2
    return res


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed.decode())
    return hashed.decode()



def compare_passwords(password, hashed_password):
    print(password)
    return bcrypt.hashpw(password.encode('utf-8'), hashed_password) == hashed_password


def generate_jwt(payload: dict, key, minuets):
    jwt_payload = Merge(payload, {"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=minuets)})
    print(json.dumps(jwt_payload, indent=4, sort_keys=True, default=str))
    jwt_payload2 = [json.dumps(jwt_payload, indent=4, sort_keys=True, default=str)]
    return jwt.encode(
        {'data': jwt_payload2},
        key)


def decode_jwt(jwt_string, key):
    try:
        return True, jwt.decode(jwt_string, key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False, 'token has expired!'







