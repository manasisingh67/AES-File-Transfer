import socket

s = socket.socket()
host = 'localhost'
port = 60005

s.connect((host, port))
s.send("Hello server!")

with open('received_file.txt', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print((data))
        if not data:
            break
        # write data to a file
        f.write(data)
        
f.close()
print('Successfully get the file')
s.close()
print('connection closed')
