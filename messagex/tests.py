from random import random
from tabnanny import verbose
from django.test import TestCase
# https://cryptography.io/en/latest/hazmat/primitives/
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import codecs
'''

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
'''

from xkcdpass import xkcd_password as xp
import random
import string

wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=15, valid_chars='.')
#print(mywords)
# create a password with the acrostic "face"
acrostic_string = "I like this site very much!"
acrostic_string.strip("!").split(" ")
for item in acrostic_string.strip("!").split(" "):
    #print(item)
    pass1=xp.generate_xkcdpassword(mywords,interactive=False, acrostic=item.lower(), delimiter="|", case="alternating", numwords=6)
    #print(pass1)

password=xp.generate_xkcdpassword(mywords,interactive=False, acrostic=False, delimiter="|", case="alternating", numwords=6)
pre_pass=password
password.split('|')
final_pass, full_pass = '', ''
choices=string.punctuation+ string.digits
print(choices)
for char in password.split('|'):
    rand_char = random.choice(choices)
    #pre_pass.replace('|', rand_char)
    final_pass+=char[0] + rand_char
    full_pass+=char + " " + rand_char + " "

    #print(char[0])
    #print(rand_char)
print(final_pass)
print(pre_pass)
print(len(final_pass))
print("This a 12-char password long: " + final_pass)
print("Remember your password as: " + full_pass)
#https://www.security.org/how-secure-is-my-password/