import requests

def get_attachment_by_id(attachment_id):
    # your code here
    url='https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    resp=requests.get(url).json()
    for i in range(0, len(resp['posts'])):
        for x in range(0, len(resp['posts'][i]['attachments'])):
            if attachment_id==resp['posts'][i]['attachments'][x]['id']:
                return resp['posts'][i]['attachments'][x]
            else:
                return 'ID or attachment does not exist'


print(get_attachment_by_id(137))