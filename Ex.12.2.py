#Exercise 2
import socket 

#Enter URL
website = input('Enter URL: ')
parts = website.split('/')
domain = parts[2]
path = '/' + '/'.join(parts[3:])

#Create Socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain,80))

#Create and send request
cmd = f'GET {path} HTTP/1.0\r\nHost: {domain}\r\n\r\n'.encode()
mysock.send(cmd)

#Receive data 
count = 0
output = ''

while True:
    data = mysock.recv(512) 
    if len(data) < 1:
        break
    statement = (data.decode())

    remaining_char = 500 - count
    if len(statement) > remaining_char:
        output += statement[:remaining_char]
        count += remaining_char
    else:
        output += statement
        count += len(statement)

print(output)
print('Count: ', count)
mysock.close()
