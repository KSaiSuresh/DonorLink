from flask import Flask, request, jsonify
from log_config import setup_logger
from mfa import verify_otp
app = Flask(__name__)

# Enable logging
global logging
logging = setup_logger()


# Routes for authentication
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email and password:
        #logic block
        success="dummy"
        if success:
            return jsonify({'message': 'User registered successfully'}), 200
        return jsonify({'message': 'Registration failed'}), 400
    return jsonify({'message': 'Invalid request data'}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email and password:
        #logic block
        success = "dummy"
        if success['is_loggedin']:
            logging.info(f'login success :{success}')
            return jsonify(success), 200
        logging.error(f'nvalid credentials HTTP : 401')
        return jsonify(success), 401
    logging.error(f'Invalid request data HTTP : 400')
    return jsonify({'message': 'Invalid request data'}), 400


@app.route('/mfaVerify', methods=['POST'])
def mfaVerify():
    data=request.get_json()
    logging.info(f"mfa code infput {data['mfa']}")
    output = verify_otp(data['mfa'])
    logging.info(f"mfa verification {output}")
    return output , 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')