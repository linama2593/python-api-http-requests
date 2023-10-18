import requests

post={'id': 123, 'title':'Very big project'}
resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json=post)
print(resp.text)