# You are a hecker. You have data that is encrypted by stealing the transmitted data, and you know that this data is in plain text.
# You need to find out the original data and the secret key (8bits).

data = '6e5253491a5e5b4e5b1a53491a5b5649551a4c5f48431a53574a55484e5b544e1a4e5f424e1a5e5b4e5b141a6a565f5b495f1a4e5b515f1a595b485f1a4d525f541a525b545e5653545d14'


import binascii

secret_key = -1
original_data = ""
max_space_characters = 0

for k in range(256):
    decoded_data = ''
    encoded_data_byte = binascii.unhexlify(data)
    for byte in encoded_data_byte:
        decoded_data += chr(byte ^ k)
    num_space_characters = decoded_data.count(' ')
    if num_space_characters > max_space_characters:
        max_space_characters = num_space_characters
        secret_key = k
        original_data = decoded_data

print("{0:b}".format(secret_key).zfill(8))
print(original_data)