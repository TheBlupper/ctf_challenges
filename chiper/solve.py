from base64 import b64decode
from ascii_chiper import Chiper

ct = '0Z9Hz9ImSqzsDYze83TuRNlBExCIjTw9HqvNoEwh5vibcWA9Mtf8M+Cl33/pCAwlwuH5qh47RCLBzqhMrI6+5bYf0ZEmBEwYOPsaKz4VwXHRV0fP0qxK4+xkjBnzk+4e2dYT0ohPPPwezs2yTFDmDZulYLkytfxE4HXfLOmVDPXCEvkMHtNEvsHcqBGsE775tovRoiaYTKI4YhqhPt3B3g=='

chiper = Chiper.initialize()
base, length = 113, 40

# You need to do an encryption first otherwise decryption errors...
chiper.encrypt('a', base, length, Chiper.FULL_ENCRYPTION)

key = list(b64decode(ct)[::-1][1::2])
print(chiper.decrypt(ct, key=key, decrypt_steps=Chiper.FULL_ENCRYPTION))