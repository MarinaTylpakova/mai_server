import socket
import random

sock = socket.socket()
sock.bind(('localhost', 8000))    
sock.listen(1)          
conn, addr = sock.accept()  

print('connected:', addr)

number = random.randint(0, 10)
print(number)

while True:
    number1 = conn.recv(1024)  
    number1 = number1.decode('utf-8')
    if not number1:
        break

    num = int(number1, 10)
    if num < number:
        resp = 'less'
    if num > number:
        resp = 'more'
    if num == number:
        resp = 'correct'
    resp = resp.encode('utf-8')
    conn.send(resp)

conn.close()