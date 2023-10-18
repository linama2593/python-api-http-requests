import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
dic=response.json()

print('Current time: '+str(dic['hours'])
      +' hrs '+str(dic['minutes'])+' min and '+
       str(dic['seconds'])+' sec' )