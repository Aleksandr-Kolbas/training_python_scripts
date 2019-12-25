import requests


def get_math_fact_from_api():
    """Shows an interesting math fact (if any) about the requested number
    from the API of the website http://numbersapi.com/"""
    number = int(input('Enter the number you want to know about: '))
    api_url = "http://numbersapi.com/{}/math?json=true".format(number)
    res_from_api = requests.get(api_url)
    data_in_json = res_from_api.json()
    if data_in_json['found']:
        print(data_in_json['text'])
    else:
        print('Boring number. Nothing interesting.')


get_math_fact_from_api()
