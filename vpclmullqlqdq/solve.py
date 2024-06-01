from sage.all import *
from pwn import bits, unbits

x = var('x')
# quotienting by x**64 <=> truncating to 64 bits
R, x = GF(2)['x'].quotient(x**64).objgen()

to_poly = lambda by: R(bits(by, 'little'))
to_bytes = lambda p: unbits(p, 'little')

M = [0xcc89e1f8f24f2b9d, 0xd4fec89b998c561f, 0xf4e28091ebae53ee, 0xf5489cf52df5731a,
     0x9a79638701bc09f4, 0xcfd371c5f0b2067a, 0xb1eb90251a93f191, 0xa528ef3e9c7b7dcf,
     0xb557ccbda3963606, 0xaaf942eb86c1eab5, 0xec980862749e5134, 0xb6eaf6bdc5012fa7,
     0xbf2ed7c70db689c8, 0xfcf155f62004fd02, 0x98f89bbfaf61c3a5, 0xb04c1ddff4b6a57e]
tgt = [0x6e4449f923c50d94, 0xe5eaea1483ecf196, 0x9101d886548c0659, 0x1633fb78701720ac]

conv = lambda n: to_poly(n.to_bytes(8, 'little'))
M = matrix(R, 4, 4, list(map(conv, M)))
tgt = vector(R, map(conv, tgt))
print(b''.join(to_bytes(p) for p in M**-1 * tgt))