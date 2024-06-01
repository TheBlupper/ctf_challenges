import os
from keystone import *
from pwn import bits, unbits, u32, u64
from sage.all import *

flag = b'SECFEST{5ry_f0r_b31ng_4nn0y1ng.}'
assert len(flag) == 32

set_random_seed(0)

# truncating to 64 bits is equivalent to modding by x^64
x = var('x')
R, x = GF(2)['x'].quotient(x**64).objgen()

to_poly = lambda by: R(bits(by, 'little'))
to_bytes = lambda p: unbits(p, 'little')

while True:
    M = matrix(R, 4, 4, lambda *_: R.random_element())
    if M.is_invertible(): break

flag_vec = vector([to_poly(flag[i:i+8]) for i in range(0, 32, 8)])

enc = [to_bytes(p) for p in M*flag_vec]

asm = '''
; r15 is input array
; r14 is output array
; r13 is the length of the input
; r12 is if we have failed
mov rax, 0
mov rdi, 0
mov rsi, r15
mov rdx, 32
syscall
xor r12, r12

; bad  
mov ebx, 0x000a283a
mov [r14], ebx
; good
mov ebx, 0x000a293a
mov [r14+4], ebx
'''

for i in range(4):
    asm += f'''
; load target into rdi
mov edi, {u32(enc[i][4:])}
shl rdi, 32
mov ebx, {u32(enc[i][:4])}
or rdi, rbx
'''
    
    for j in range(4):
        coeff = to_bytes(M[i, j])
        asm += f'''
; load coefficient into rdx
mov edx, {u32(coeff[4:])}
shl rdx, 32
mov ebx, {u32(coeff[:4])}
or rdx, rbx

; multiply
movq xmm2, rdx
vpclmulqdq xmm2, xmm2, [r15+{8*j}], 0

; add
movq rdx, xmm2
xor rdi, rdx
'''
    asm += f'''
; check
mov rbx, 1
cmovne r12, rbx
'''
    

asm += '''
; load output string
mov rsi, r14
lea rbx, [r14+4]
test r12, r12
cmove rsi, rbx

; write
mov rax, 1
mov rdi, 1
mov rdx, 4
syscall

; exit
mov rax, 60
mov rdi, 0
syscall
'''

block_sz = 7

ks = Ks(KS_ARCH_X86, KS_MODE_64)
instrs = []
for line in asm.splitlines():
    if line.startswith(';'): continue
    if not line: continue
    instr = ks.asm(line)[0]
    if len(instr) > block_sz: raise ValueError('too long instruction')
    instrs.append(bytes(instr))

prev = b'\x5d' + b'\x90'*7
out = b''
while instrs:
    segment = instrs.pop(0)
    while len(instrs) and len(segment + instrs[0]) < block_sz:
        segment += instrs.pop(0)
    segment = b'\x5d' + segment.ljust(block_sz, b'\x90')
    out += to_bytes(to_poly(segment) / to_poly(prev))
    prev = segment

with open('template.asm', 'r') as f:
    src = f.read()

with open('chall.asm', 'w') as f:
    f.write(src.replace('REPLACE', str(list(out))[1:-1]))

os.system('nasm -f elf64 chall.asm -o chall.o')
os.system('ld -Ttext=0x1337080 -s --omagic chall.o -o ./dist/chall')
os.system(f'echo {flag.decode()} | ./dist/chall')