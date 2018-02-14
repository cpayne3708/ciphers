alphabet = "abcdefghijklmnopqrstuvwxyz\\`~!@#$%^&*()-_=+[{]}|;:'\",<.>/?ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
key = " `~!@#$%^&*()-_=+[{]}|;:'\"<,.>/?\\poiuytrewqasdfghjklmnbvcxz0987654321POIUYTREWQASDFGHJKLMNBVCXZ"

def encrypt(msg):
    new = ""
    for c in msg:
        new += key[alphabet.find(c)]


    return new

def decrypt(msg):
    new = ""
    for c in msg:
        new += alphabet[key.find(c)]

    return new

msg = "\"enCrYPt a sEnTeNCe\" on 2/14/2018"
encrip = encrypt(msg)
decrip = decrypt(encrip)

print(msg)
print(encrip)
print(decrip)

