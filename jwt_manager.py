from jwt import encode, decode

def generate_token(payload, secret):
    token : str = encode(payload, secret, algorithm='HS256')
    return token

def validate_token(token, secret):
    return decode(token, secret, algorithms=['HS256'])


                  