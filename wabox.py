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
*Grosir Pengharum Ruangan/Mobil Multiguna Murah!!!*

Welcome Reseller!!dropshipper!!dan terima partai besar!! Parfum Pewangi / pengharum aroma ruangan, Mobil, toilet dll.. 

Ada 13 Varian aroma : 
1. Coffee = aroma kopi 
2. Lemon = aroma lemon 
3. Bubble Gum = aroma permen karet
4. Vanila = aroma vanila
5. Sweet Army = aromanya strong (warna hijau) 
6. Sweet honey = aromanya medium (warna merah) 
7. Sweet fresh = aromanya soft (warna biru / ungu) 
8. Green tea
9. Sweet apple
10. Sweet strawberry
11. Sweet Lecy
12. Sweet manggo
13. Cappucino

*Eceran Rp 15.000 per pc*

Harga grosir!!! 
*10-100 pcs harga Rp 11.000 per pc*
*Diatas 100 pcs harga Rp 10.000 per pc*
Boleh campur2 Varian Aroma!! 
Non Alkohol!!
_Lihat contoh gambar pada Profile Photo_

COD hanya untuk area Cipinang, Duren Sawit, Pondok Kelapa, Pondok Bambu, Buaran
contact : *0813 8206 2955*
IG : *@shopnshopperz*
"""


#Message saja
for i in range(rg):

    uid = str(uuid.uuid1())
    data = urllib.urlencode({
        "token": token,
        "uid": "6281282632197",
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
