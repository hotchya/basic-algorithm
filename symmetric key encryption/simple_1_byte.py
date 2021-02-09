import binascii

def xor_1(data:bytearray, key:int)->bytearray:
    r = bytearray()
    for b in data:
        r.append(b^key)
    return r

data = 'This data is very important text data. Take care when handling.'
key = "10101111"

encoded = xor_1(data.encode(),int(key, 2))
print(binascii.hexlify(encoded))

decoded = xor_1(encoded,int(key, 2))
print(decoded.decode())