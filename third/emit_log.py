#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel() # access to  queue a random name
# channel.queue_declare(queue='', exclusive=True) - once the consumer connection is closed, the queue should be deleted. 

# The exchange parameter is the name of the exchange
# fanout - broadcast log messages to many receivers.
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message) 
print(f" [x] Sent {message}")
connection.close()
