import requests

api_pokemon = 'https://pokeapi.co/api/v2/pokemon/1'


def teste_get():
    response = requests.get(url=api_pokemon)

    status_code = response.status_code

    assert status_code == 200


def teste_post():
    payload = dict(key1='value1', key2='value2')
    response = requests.post('https://httpbin.org/post', data=payload)

    status_code = response.status_code

    assert status_code == 200
