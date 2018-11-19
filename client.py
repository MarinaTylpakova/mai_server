import socket
import random

sock = socket.socket()
sock.connect(('localhost', 8000))
min_border = 0
max_border = 10

while True: 

        number = random.randint(min_border, max_border)
        print(number)
        str1 = str(number)

        number1 = str1.encode('utf-8')
        sock.send(number1)

        resp = sock.recv(1024)
        resp = resp.decode('utf-8')
        print(resp)

        if resp == 'less':
            min_border = number + 1

        if resp == 'more':
            max_border = number - 1

        if resp == 'correct':
            break

sock.close()

