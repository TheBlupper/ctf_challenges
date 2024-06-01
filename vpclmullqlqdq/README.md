# vpclmullqlqdq
> Really rolls of the tongue doesn't it?

This challenge makes heavy use of the x86 instruction with the same name, which is part of the [CLMUL instruction set](https://en.wikipedia.org/wiki/CLMUL_instruction_set). As can be seen on Wikipedia, "carry-less multiplication" (which is what the function does) can be seen as interpreting the bits of two numbers as coefficients in two polynomials and then multiplying the polynomials modulo 2 (i.e in $\text{GF}(2)$ ).

It decrypts a blob of data via use of this instruction, this can be pretty easily recovered by stepping through the program of writing a small decryption program yourself. The result is shellcode which is executed, which when decompiled with Binary Ninja looks like this:
```c
void sub_0(int32_t* out @ r14, void* inp @ r15, int64_t arg3, int64_t arg4, int64_t arg5, int64_t arg6, int64_t arg7, int64_t arg8) __noreturn
{
    syscall(sys_read {0}, 0, inp, 0x20);
    int64_t loose = 0;
    *(uint32_t*)out = ':(\n';
    out[1] = ':)\n';
    if ((((0x6e4449f923c50d94 ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x33761e070db0d463, *(uint128_t*)inp, 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x2b0137646673a9e1, *(uint128_t*)((char*)inp + 8), 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0xb1d7f6e1451ac12, *(uint128_t*)((char*)inp + 0x10), 0)) != __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0xab7630ad20a8ce6, *(uint128_t*)((char*)inp + 0x18), 0))
    {
        loose = 1;
    }
    if ((((-0x1a1515eb7c130e6a ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x65869c78fe43f60c, *(uint128_t*)inp, 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x302c8e3a0f4df986, *(uint128_t*)((char*)inp + 8), 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x4e146fdae56c0e6f, *(uint128_t*)((char*)inp + 0x10), 0)) != __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x5ad710c163848231, *(uint128_t*)((char*)inp + 0x18), 0))
    {
        loose = 1;
    }
    if ((((-0x6efe2779ab73f9a7 ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x4aa833425c69c9fa, *(uint128_t*)inp, 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x5506bd14793e154b, *(uint128_t*)((char*)inp + 8), 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x1367f79d8b61aecc, *(uint128_t*)((char*)inp + 0x10), 0)) != __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x491509423afed059, *(uint128_t*)((char*)inp + 0x18), 0))
    {
        loose = 1;
    }
    if ((((0x1633fb78701720ac ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x40d12838f2497638, *(uint128_t*)inp, 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x30eaa09dffb02fe, *(uint128_t*)((char*)inp + 8), 0)) ^ __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x67076440509e3c5b, *(uint128_t*)((char*)inp + 0x10), 0)) != __vpclmulqdq_xmmdq_xmmdq_memdq_immb(-0x4fb3e2200b495a82, *(uint128_t*)((char*)inp + 0x18), 0))
    {
        loose = 1;
    }
    int32_t* out_1 = out;
    if (loose == 0)
    {
        out_1 = &out[1];
    }
    syscall(sys_write {1}, 1, out_1, 4);
    syscall(sys_exit {0x3c}, 0);
    /* no return */
}
```

Here the result of each polynomial multiplication is actually truncated; only the lower 64 bits of each result is used. Furthermore, XOR:ing in this context is actually equivalent to adding two polynomials and then taking mod 2. This means that each of the 4 clauses above are actually linear equations in our input, if you consider it to be in the ring $\text{GF}(2)[x]/(x^{64})$. $\text{GF}(2)[x]$ is just the ring of polynomials with coefficients in $\text{GF}(2)$, and then we quotient (think of it as working modulo) by $x^{64}$. This is equivalent with truncating to the lower 64 bits (whenever a polynomials degree is greater than 64 the upper terms can be subtracted away by some multiple of $x^{64}$).

Thanks to how generic Sage's tools are we can easily construct this ring and then solve the system of equations by taking a matrix inverse. See [my solve script](./solve.py).

Alternatively you can just use z3 lol.