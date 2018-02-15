alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\\`~!@#$%^&*()-_=+[{]}|;:'\",<.>/? "

def encrypt(msg,shift):
    new = ""
    for c in msg:
        index = alphabet.find(c) + shift
        if index > len(alphabet) - 1:
            index -= len(alphabet)
        new += alphabet[index]

    return new

def decrypt(msg,shift):
    new = ""
    for c in msg:
        index = alphabet.find(c) - shift
        if index < 0:
            index += len(alphabet)
        new += alphabet[index]

    return new

msg = "nick dont know how to do this #dummy #prollygota55intheclass"
encrip = encrypt(msg,3)
decrip = decrypt(encrip,3)


print(msg)
print(encrip)
print(decrip)

