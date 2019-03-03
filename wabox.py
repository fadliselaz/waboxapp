import urllib
import urllib2
import uuid

with open("contact.txt", "r") as of:
    sl = of.read().split()
    
token = "1f413e0f2868ed11a1ad5c2472a2a1c85c7b88ab1f337"
contact = sl
rg = len(contact)
msg = """
*Jokowi For Indonesia*

Inilah keberhasilan Pak Jokowi
dalam pembangunan Indonesia
dalam kurun waktu 5 Tahun..

*LANJUTKAN..!!!*

_send with Whatsapp API_

"""

for i in range(rg):
    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281213655573",
        "to": contact[i],
        "custom_uid": uid,
        "text": msg
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/chat', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format(contact[i]))


for i in range(rg):
    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281213655573",
        "to": contact[i],
        "custom_uid": uid,
        "url": "https://www.instagram.com/jokowi.marufamin2019/?hl=id",
        "description" : "Pembangunan Merata di Indonesia",
        "caption" : "*keberhasilan Jokowi dalam 5 Tahun ini..*",
        "url_thumb": "https://www.dw.com/image/45315111_303.jpg",
      
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/link', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format(contact[i]))
