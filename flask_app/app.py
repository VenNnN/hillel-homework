#!python3
from flask import Flask
from flask import request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/whoami/")
def whoami():
    user_agent = request.headers['user-agent']
    requester_ip = request.remote_addr
    time_now = datetime.now().time()
    return f"Client browser: {user_agent} --|-- Client ip: {requester_ip} --|-- Time now: {time_now}"


@app.route('/source_code/')
def source_code():
    code = []
    with open(__file__, 'r') as file:
        return f"<plaintext>{file.read()}"

@app.route("/random")
def random_request():
    length = request.args.get('length')
    specials = request.args.get('specials')
    digits = request.args.get('digits')

    if (int(length) < 1 or int(length) > 100) or (specials != '0' and specials != '1') or (digits != '0' and digits != '1'):
        return f"Incorrect! Write correct length(1-100)/specials(0-1)/digits(0-1) please!"

    list_all_symbols = list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58)) + list(range(33, 48))
    result = ''
    for i in range(1, int(length)+1):
        if int(specials) == 0 and int(digits) == 0:
            result += chr(list_all_symbols[random.randint(0, 51)])
        if int(specials) == 0 and int(digits) == 1:
            result += chr(list_all_symbols[random.randint(0, 61)])
        if int(specials) == 1 and int(digits) == 0:
            rand_ind = random.randint(0, 66)
            if rand_ind > 51:
                rand_ind += 10
            result += chr(list_all_symbols[rand_ind])
        if int(specials) == 1 and int(digits) == 1:
            result += chr(list_all_symbols[random.randint(0, 76)])
    return f"{result}"

if __name__ == '__main__':
    app.run(debug=True)