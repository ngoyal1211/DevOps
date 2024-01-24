import requests

def test_shuffle_endpoint():
    input_list = [1, 2, 3, 4, 5]
    response = requests.get('http://127.0.0.1:5000/shuffle', json={'list_of_ints': input_list})