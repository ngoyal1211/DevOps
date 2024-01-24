from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/shuffle', methods=['GET'])
def shuffle():
    data = request.get_json()
    input_list = data['list_of_ints']
    shuffled_list = random.sample(input_list, len(input_list))
    response = {'shuffled_list': shuffled_list}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)