import requests

# your code here
url='https://assets.breatheco.de/apis/fake/sample/project_list.php'

res=requests.get(url).json()
res
################################
print(res[1]['name'])