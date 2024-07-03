#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',          # exchange_point
                      routing_key='hello',  # the name of queue
                      body='Hello World!')  # data  to put in queue 
print(" [x] Sent 'Hello World!'")
connection.close()
