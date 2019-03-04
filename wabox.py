import urllib
import urllib2
import uuid

with open("contact.txt", "r") as of:
    sl = of.read().split()
    
token = "1f413e0f2868ed11a1ad5c2472a2a1c85c7b88ab1f337"
contact = sl
rg = len(contact)
msg = """
*Visit labuan Bajo 2019*

Destinasi Favorit 
turis lokal dan mancanegara.

Surga di Timur Indonesia,
kunjungi Web Resmi Kami
dibawah ini..

_Otoritas Pariwisata Labuan Bajo_

"""

for i in range(rg):
    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281213655573",
        "to": "62" + contact[i],
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
        "to": "62" + contact[i],
        "custom_uid": uid,
        "url": "https://www.indonesia.travel/gb/en/destinations/bali-nusa-tenggara/labuan-bajo",
        "description" : "Destinasi Wisata di Timur Indonesia",
        "caption" : "Visit Labuan Bajo 2019",
        "url_thumb": "https://www.indonesia.travel/content/dam/indtravelrevamp/en/destinations/bali-nusa-tenggara/east-nusa-tenggara/labuan-bajo/LB1.jpg",
      
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/link', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format("62" + contact[i]))
