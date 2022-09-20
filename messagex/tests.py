from django.test import TestCase
# https://cryptography.io/en/latest/hazmat/primitives/
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import codecs

data = b"a secret message"
print('data:' + data.decode())
authentication = b"authenticated but unencrypted data"
print('authentication:' + authentication.decode())
key = AESGCM.generate_key(bit_length=256)
print('key:' + bytes(key).hex())
aesgcm = AESGCM(key)
nonce = os.urandom(12)
print('nonce:' + bytes(nonce).hex())
cyphertext = aesgcm.encrypt(nonce, data, authentication)
print('cyphertext:' + bytes(cyphertext).hex())
originaldata = aesgcm.decrypt(nonce, cyphertext, authentication)
print('originaldata:' + originaldata.decode())
