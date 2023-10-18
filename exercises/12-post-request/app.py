import requests

# your code here
url='https://assets.breatheco.de/apis/fake/sample/post.php'

data = {'Name': 'Carol'}

post = requests.post(url, json = data)

print(post.text)