import urllib
import urllib2
import uuid

with open("contact.txt", "r") as of:
    sl = of.read().split()
    
token = "1f413e0f2868ed11a1ad5c2472a2a1c85c7b88ab1f337"
contact = sl
rg = len(contact)
msg = """
*Tahukah Anda?*

1. Bahwa biaya perawatan kamar (saja) di Rumah Sakit Singapore bisa mencapai *$688 per- malamnya?* Dan itu setara dengan *Rp.7,2 Juta??*

2. Bahwa Allianz menanggung semua biaya perawatan, obat, operasi, donor transplantasi, pendamping, dll, sesuai tagihan dengan limit hingga 25 M??

3. Bahwa dengan setoran FLAT Premi Rupiah, Allianz akan menanggung biaya Rumah sakit dalam bentuk Dollar hingga ke seluruh dunia?

*Yuni Pratiwi*
Financial Advisor
081311009769
Allianz Life Indonesia
_Happily Helping Others_

"""


#Message saja
for i in range(rg):
    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281932006544",
        "to": "62" + contact[i],
        "custom_uid": uid,
        "text": msg
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/chat', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format(contact[i]))

    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281932006544",
        "to": "62" + contact[i],
        "custom_uid": uid,
        "url": "https://gdurl.com/ZUHC/download",
        "description" : "Allianz Life Indonesia - Happily Helping Others",
        "caption" : "Tahukah Anda ?",
        "url_thumb" : "https://gdurl.com/Jt49",
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/link', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format("62" + contact[i]))


# image with link and description
# for i in range(rg):
#     uid = str(uuid.uuid1())
#     data = urllib.urlencode({
#         "token": token,
#         "uid": "6281932006544",
#         "to": "62" + contact[i],
#         "custom_uid": uid,
#         "url": "https://www.indonesia.travel/gb/en/destinations/bali-nusa-tenggara/labuan-bajo",
#         "description" : "Destinasi Wisata di Timur Indonesia",
#         "caption" : "Visit Labuan Bajo 2019",
#         "url_thumb": "https://www.indonesia.travel/content/dam/indtravelrevamp/en/destinations/bali-nusa-tenggara/east-nusa-tenggara/labuan-bajo/LB1.jpg",
      
#     })

# any file
# for i in range(rg):
#     uid = str(uuid.uuid1())
#     data = urllib.urlencode({
#         "token": token,
#         "uid": "6281932006544",
#         "to": "62" + contact[i],
#         "custom_uid": uid,
#         "url": "https://gdurl.com/ZUHC/download",
#         "description" : "Allianz Life Indonesia - Happily Helping Others",
#         "caption" : "Tahukah Kamu ?",
#         "url_thumb" : "https://gdurl.com/Jt49",
#     })

#     req = urllib2.Request('https://www.waboxapp.com/api/send/link', data)
#     response = urllib2.urlopen(req)
#     result = response.read()

#     print("succes send to {}".format("62" + contact[i]))
