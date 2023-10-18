import requests

# your code here
url='https://assets.breatheco.de/apis/fake/sample/project1.php'

resp=requests.get(url).json()

print(resp['name'])
