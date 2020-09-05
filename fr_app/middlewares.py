import json
from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions


def login_required(f):

    @wraps(f)
    def wrap(*args, **kwargs):
        authorization = request.headers.get("Authorization-Code", None)
        if not authorization:
            return json.dumps({'error': 'No authorization token provied'}), 401, {'Content-type': 'application/json'}
        try:
            token = authorization.split(' ')[1]
            resp = decode(token, None, verify=False, algorithms=['HS256'])
            g.user = resp['sub']
        except Exception as ex:
            return json.dumps({'error': 'Invalid authorization token'}), 401, {'Content-type': 'application/json'}
        return f(*args, **kwargs)
    return wrap
