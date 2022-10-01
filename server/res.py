from flask import make_response, jsonify

def res(json, status_code):
    response = make_response(jsonify(json), status_code)
    response.headers['Content-Type'] = 'application/json'
    return response
