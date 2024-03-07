from socket import socket, AF_INET, SOCK_STREAM

# Socket creation
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 12345))
s.listen(5)

while True:
    # Accept connection
    client, addr = s.accept()

    # Read HTTP request from socket
    request = client.recv(4096)
    print(
        request)

    # Construct HTML response
    html_response = b'HTTP/1.1 200 OK\n'
    html_response += b'Content-Type: text/html\n'
    html_response += b'Access-Control-Allow-Origin: *\n'
    html_response += b'\n'
    html_response += b'<html><body>'
    html_response += b'<p><b>Hello</b> <u>world</u></p>'
    html_response += b'</body></html>'

    # Send HTML response to client
    client.send(html_response)
    client.close()
