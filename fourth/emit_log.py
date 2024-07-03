#!/usr/bin/env python
import pika
import sys

# Установка соединения
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Создание канала
channel = connection.channel()

# Create exchange point
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# a message goes to the queues whose binding key exactly matches the routing key of the message.
channel.basic_publish(
    exchange='direct_logs', 
    routing_key=severity, #  
    body=message
)
print(f" [x] Sent {severity}:{message}")
connection.close()
