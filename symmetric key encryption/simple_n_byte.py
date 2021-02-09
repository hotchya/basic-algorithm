import binascii

def xor_2(data:bytes, key:bytes, k_len)->bytearray:
    r = bytearray()
    for i in range(len(data)):
        k = key[i % k_len]
        r.append(data[i] ^ k)
    return r

data = 'This data is very important text data. Take care when handling.'
key = 'secretKey'

encoded = xor_2(data.encode(),key.encode(),len(key))
print(binascii.hexlify(encoded))

decoded = xor_2(encoded,key.encode(),len(key))
print(decoded.decode())