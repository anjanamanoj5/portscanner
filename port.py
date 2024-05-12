import sys
import socket
print("enter ip")
inp=input()
target = socket.gethostbyname(inp)
for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        out = s.connect_ex((target,port))
        if out ==0:
            print("open ",port)
        s.close()