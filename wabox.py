import urllib
import urllib2
import uuid
import time

with open("contact.txt", "r") as of:
    sl = of.read().split()
    
token = "1f413e0f2868ed11a1ad5c2472a2a1c85c7b88ab1f337"
contact = sl
rg = len(contact)
msg = """
*Service Handphone Bergaransi*
*ADE - CELL*

Terima Service Handphone,
-upgrade software,
-boodlop stock logo,
-lupa pola,
-battray,
-accesoris
-mati total,
-ganti touchscreen lcd,
-instal laptop cpu,
-pulsa,token listrik
-dan lain lainnya.

 *KAMI SIAP MELAYANI ANDA 
 DENGAN SENANG HATI.*

Jl. Tegal Parang Selatan 1
no 5b.
Buka Setiap hari
jam 7pagi - 12 malam.

"""


#Message saja
for i in range(rg):

    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281213655573",
        "to": "62" + contact[i],
        "custom_uid": uid,
        "text" : msg,
    })

    req = urllib2.Request('https://www.waboxapp.com/api/send/chat', data)
    response = urllib2.urlopen(req)
    result = response.read()

    print("succes send to {}".format(contact[i]))
    print("message terkirim: {}".format(i+1))
    time.sleep(10)


# image with link and description
# for i in range(rg):
#     uid = str(uuid.uuid1())
#     data = urllib.urlencode({
#         "token": token,
#         "uid": "6281282632197",
#         "to": "62" + contact[i],
#         "custom_uid": uid,
#         "url": "https://www.instagram.com/p/BvUKJ97pVsu/?utm_source=ig_share_sheet&igshid=1tyuu1yswpnnv",
#         "description" : "Pengharum Ruangan Murah",
#         "caption": "Pengharum Ruangan Murah..",
#         "url_thumb": "https://gdurl.com/S6oE",
      
#     })

#     req = urllib2.Request('https://www.waboxapp.com/api/send/link', data)
#     response = urllib2.urlopen(req)
#     result = response.read()


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


#     print("succes send to {}".format("62" + contact[i]))
