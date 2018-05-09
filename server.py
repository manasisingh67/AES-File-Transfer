import socket

port = 7702
s = socket.socket()
host = socket.gethostname()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(5)

print 'Server listening....'

while True:
    conn, addr = s.accept()
    print 'Got connection from', addr
    l = conn.recv(1024)
    print repr(l)

    filename='text.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print repr(l)
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
