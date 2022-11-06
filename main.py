import requests
import time
f2 = open('result.txt', 'w', encoding="utf8")
# Hello, my name is Semjon, this is my testwork and I didn't create a good working code :)) And I tried to read PHP and Java Client.
# Well I starting the description.
# Below you can find the method by which I tried to connect and call authorization,
# but the server gives a 400 error, although there is a certificatechoice method with the same parameters, then everything works.
param = {
  "relyingPartyUUID": "00000000-0000-0000-0000-000000000000",
  "relyingPartyName": "DEMO",
  "certificateLevel": "QUALIFIED",
  "hash": "ZHNmYmhkZmdoZGcgZmRmMTM0NTM...",#I not understend wat this
  "hashType": "SHA512",
  "allowedInteractionsOrder": [
    {
      "type": "displayTextAndPIN",
      "displayText60": "Test123"
    }
  ]
}
url = "https://sid.demo.sk.ee/smart-id-rp/v2/authentication/etsi/PNOEE-30303039914"
respons = requests.post(url, json=param)
print(respons)
# Therefore, I wrote what should work in theory - give the correct parameters and compose the url address
param = {
  "relyingPartyUUID": "00000000-0000-0000-0000-000000000000",
  "relyingPartyName": "DEMO",
  "certificateLevel": "QUALIFIED",
  "hash": "ZHNmYmhkZmdoZGcgZmRmMTM0NTM...",#I not understend wat this
  "hashType": "SHA512",
  "allowedInteractionsOrder": [
    {
      "type": "displayTextAndPIN",
      "displayText60": "Test123"
    }
  ]
}
url = "https://sid.demo.sk.ee/smart-id-rp/v2/authentication/etsi/PNOEE-30303039914"
sesionID = requests.post(url, json=param).text[14:50]
f2.write(sesionID + '\n')

time.sleep(5)
url = f"https://sid.demo.sk.ee/smart-id-rp/v2/session/{sesionID}"
otv = requests.get(url).text
f2.write(otv + '\n')

time.sleep(15)
url = f"https://sid.demo.sk.ee/smart-id-rp/v2/session/{sesionID}"
otv = requests.get(url).text
f2.write(otv + '\n')
#well that end))
#May be I not good read documentation or maybe not good creating
