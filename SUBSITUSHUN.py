alphabet = "abcdefghijklmnopqrstuvwxyz\\`~!@#$%^&*()-_=+[{]}|;:'\",<.>/?ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
key = " `~!@#$%^&*()-_=+[{]}|;:'\"<,.>/?\\poiuytrewqasdfghjklmnbvcxz0987654321POIUYTREWQASDFGHJKLMNBVCXZ"

def encrypt(string):
    new = ""
    for c in string:
        new += key[alphabet.find(c)]


    return new

def decrypt(string):
    new = ""
    for c in string:
        new += alphabet[key.find(c)]

    return new

msg = "\"enCrYPt a sEnTeNCe\" on 2/14/2018"
encrip = encrypt(msg)
decrip = decrypt(encrip)

print(msg)
print(encrip)
print(decrip)

