from ascii_chiper import Chiper # https://pypi.org/project/ascii-chiper/
print(Chiper.initialize().encrypt(open('flag.txt', 'r').read(), 113, 40, Chiper.FULL_ENCRYPTION))
# 0Z9Hz9ImSqzsDYze83TuRNlBExCIjTw9HqvNoEwh5vibcWA9Mtf8M+Cl33/pCAwlwuH5qh47RCLBzqhMrI6+5bYf0ZEmBEwYOPsaKz4VwXHRV0fP0qxK4+xkjBnzk+4e2dYT0ohPPPwezs2yTFDmDZulYLkytfxE4HXfLOmVDPXCEvkMHtNEvsHcqBGsE775tovRoiaYTKI4YhqhPt3B3g==