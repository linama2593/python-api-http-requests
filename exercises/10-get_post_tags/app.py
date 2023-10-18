import requests

def get_post_tags(post_id):
    # your code here
    url='https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    resp=requests.get(url).json()
    for i in range(0, len(resp['posts'])):
        if post_id==resp['posts'][i]['id']:
            return resp['posts'][i]['tags']
        else:
            return 'Post ID does not exist'

print(get_post_tags(146))