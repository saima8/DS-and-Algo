# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmH_IDCWAIurmtFadMU-5ZbUEKa3GBSR
"""

import requests

url = 'https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/access'
data = { "email": "tithi888khan@gmail.com"}

#use the 'headers' parameter to set the HTTP headers:
postResponse = requests.post(url, json = data, headers = {"x-api-key": "JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0"})

print(postResponse.text)

#the 'demopage.asp' prints all HTTP Headers

"""Access Token Generated. Its valid for next 5 minutes. Please fetch the access token by doing a GET operation on this resource as instructed. Please check the instructions given to you via email earlier for more details.

"""

accessTokenResponse = requests.get(url, headers = {"x-api-key": "JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0"})

print(accessTokenResponse.text)

getUrl = 'https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/access?email=tithi888khan@gmail.com'


#use the 'headers' parameter to set the HTTP headers:
getResponse = requests.get(getUrl, headers = {"x-api-key": "JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0"})

print(getResponse.text)

#the 'demopage.asp' prints all HTTP Headers

"""{"accessToken":"NtgkK9D0Cjk7CBNE-tithi888khan%40gmail.com-de2VdnPjkIQSUfp2","attempt":2,"accessTokenValidTillinUTC":"2021-10-29T03:46:12.843Z","instructions":{"steps":{"step1":"Congratulations! Please save your code as this will be needed in our later stage. As part of this URL response, you also get a 'urlObject' which has different properties","step2":"Construct the actual url by following this protocol by using various properties from the 'urlObject' : protocol://domain/path/resource","step3":"using the httpMethod as mentiond in the url do a REST call in the constructed URL. You need to give both of the API keys and access token in the header","step4":"header key for access token is 'accesstoken' and header key for api key is 'x-api-key' and add queryStringParameters like  protocol://domain/path/resource?email=your email","step5":"The access token is valid only for 5 minutes and once it is expired you need to regenerate the token again. You can generate token only 10 times","step6":"You will get information about more steps once you have do a successful REST call to the URL you just constructed as per step2"},"urlObject":{"protcol":"https","domain":"todn22mvx9.execute-api.ap-south-1.amazonaws.com","path":"dev","resource":"screeningForm","httpMethod":"GET"}}}"""

