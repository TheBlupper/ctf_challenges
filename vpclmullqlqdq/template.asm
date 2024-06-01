global    _start
section   .text
_start:
        mov r15, inp
        mov r14, out
        mov rsp, code

        loop:
        db 0x5d
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        movq xmm0, QWORD[rsp]
        vpclmulqdq xmm0, xmm0, OWORD [loop], 0
        movq QWORD [loop], xmm0
        jmp loop

section   .data
code: db "have fun", REPLACE
align 32
inp: times 32 db 0
out: times 8 db 0