import json
from functools import wraps
from flask import jsonify, request, abort
from auth import decode_jwt

JWT_KEY = 'key'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.cookies.get('jwt')
        except ValueError:
            token = None
        if token is None:
            return {
                "message": "Authentication Token is missing",
                "data": None,
                "error": "Unauthorized"
            }, 401
        result, payload = decode_jwt(token, JWT_KEY)

        if result is False:
            return {
                "message": "Invalid Token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        print(payload)
        data = json.loads(payload['data'][0])
        user_id = data['id']
        email = data['email']
        return f(user_id, email, *args, **kwargs)

    return decorated
