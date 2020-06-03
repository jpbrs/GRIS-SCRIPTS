#!/usr/bin/env python
import pika
from datetime import datetime, date, time
import time


# Set the connection parameters to connect to rabbit-server1 on port 5672
# on the / virtual host using the username "guest" and password "guest"

credentials = pika.PlainCredentials('jpbrs', '8908465')
parameters = pika.ConnectionParameters('127.0.0.1',5672,'/',credentials)

connection = pika.BlockingConnection(parameters) #Blocking Connection Pois funciona com RPC e a conexāo fica bloqueada até se obter a resposta da conexao 
channel = connection.channel() #O Canal de comunicao, uma classe que contêm os metodos de comunicacao

channel.queue_declare(queue='ronaldo') #A fila a qual será publicada a mensagem




while True:
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    channel.basic_publish(exchange='',
                      routing_key='ronaldo', 
                      body=str(timestamp))
    print(" [x] Sent Time")
    time.sleep(1)


connection.close()
