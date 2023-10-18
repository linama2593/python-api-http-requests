import requests

# your code here
url='https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'

resp=requests.get(url).json()

print(resp['posts'][0]['author']['name'])
