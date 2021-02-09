import binascii

def encoder(data:str, key:str) -> bytes:
    encoded_data = []
    ## xor
    for ch in data:
        result = ord(ch) ^ int(key, 2)
        encoded_data.append(result)
    ## Convert binary data to hexadecimal representation
    encoded_data_hex = binascii.hexlify(bytes(encoded_data))
    return encoded_data_hex

def decoder(encoded_data:bytes, key:str) -> str:
    decoded_data = ''
    ## Converted hexadecimal string to binary data
    encoded_data_byte = binascii.unhexlify(encoded_data)
    ## xor
    for byte in encoded_data_byte:
        decoded_data += chr(byte ^ int(key, 2))
    return decoded_data

# We use 8bits key
key = '11001010'
# Suppose the data is long text
data = 'This data is very important text data. Take care when handling.'

# Encrypt data to be transmitted.
encoded = encoder(data, key)

# Encrypted data
print(encoded)

# A secret key is required for decryption.
print(decoder(encoded,key))