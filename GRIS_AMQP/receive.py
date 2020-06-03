#!/usr/bin/env python
import pika


credentials = pika.PlainCredentials('jpbrs', '8908465')
parameters = pika.ConnectionParameters('127.0.0.1',5672,'/',credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='ronaldo')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='ronaldo', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()