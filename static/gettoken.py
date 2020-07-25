import requests, json, hashlib

publicKey = '38cd79b5f2b2486d86f562e3c43034f8'
privateKey = '8e49ff607b1f46e1a5e8f6ad5d312a80'

requestTokenURL = 'http://api.pixlpark.com/oauth/requesttoken'
accessTokenURL = 'http://api.pixlpark.com/oauth/accesstoken'
ordersURL = 'http://api.pixlpark.com/orders'

requestToken = requests.request('GET', requestTokenURL).json()['RequestToken']

passwordUnhashed = requestToken + privateKey
hashObject = hashlib.sha1(passwordUnhashed.encode('utf-8'))
password = hashObject.hexdigest()

parameters = {
    'oauth_token': requestToken,
    'grant_type': 'api',
    'username': publicKey,
    'password': password,
}

response = requests.request('GET', accessTokenURL, params=parameters)

accessToken = response.json()['AccessToken']
print(accessToken)

ordersParameters = {
    'oauth_token': accessToken
}

ordersResponse = requests.request('GET', ordersURL, params=ordersParameters)

with open('data.json', 'w') as f:
    json.dump(ordersResponse.json(), f)