#!/usr/bin/env python

import pika, sys, os
def main():
    # Установка соединения
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # Создание канала
    channel = connection.channel()
    # Создание очереди (если не существует)
    channel.queue_declare(queue='hello')
    # Функция, которая будет вызвана при получении сообщения
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
    
    # Подписка на очередь и установка обработчика сообщений
    channel.basic_consume(
            queue='hello', 
            on_message_callback=callback, 
            auto_ack=True, # Автоматическое подтверждение обработки сообщений
    )
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
