import requests

def status_check(code):
    if code==404:
        print(str(code)+': The URL you asked is not found')
    elif code==503:
        print(str(code)+': Unavailable right now')
    elif code==200:
        print(str(code)+': Everything went perfect')
    elif code==400:
        print(str(code)+': Something is wrong on the request params')
    else:
        print('anything')

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")


status_check(response.status_code)