import pika
from datetime import datetime, date, time
import time

credentials = pika.PlainCredentials('jpbrs', '8908465')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(
    exchange="test_exchange",
    exchange_type="fanout",
    passive=False,
    durable=True,
    auto_delete=False)


channel.queue_declare(queue='ronaldo')
channel.queue_declare(queue='rogerio')

channel.queue_bind(exchange="test_exchange",
                   queue='ronaldo')
channel.queue_bind(exchange="test_exchange",
                   queue='rogerio')


while True:
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    channel.basic_publish(exchange='test_exchange',
                      routing_key='', 
                      body=str(timestamp))
    print(" [x] Sent Time")
    time.sleep(1)