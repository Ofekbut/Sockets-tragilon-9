from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
dst_ip = '127.0.0.1'
dst_port = 12346
s.sendto(b'Hello', (dst_ip, dst_port))

data, sender_info = s.recvfrom(2048)
s.close()
