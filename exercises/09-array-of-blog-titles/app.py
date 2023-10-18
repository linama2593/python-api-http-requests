import requests


def get_titles():
    # your code here
  
    url='https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    resp=requests.get(url).json()
    titles=[resp['posts'][i]['title'] for i in range(0, len(resp['posts']))]
    return titles

print(get_titles())