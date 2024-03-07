from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
src_ip = ''
src_port = 12346
s.bind((src_ip, src_port))

while True:
    data, sender_info = s.recvfrom(2048)
    s.sendto(data.upper(), sender_info)
