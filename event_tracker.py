from confluent_kafka import Consumer
import json

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("Consumer is running and subscribed to the topic orders")

try:
    while True:
        message = consumer.poll(1.0)
        if message is None:
            continue
        if message.error():
            print("Consumer error:".format(message.error()))
            continue

        value = message.value().decode("utf-8")
        order = json.loads(value)
        print(f"Order received from {order['user_name']} for {order['quantity']} x {order['dish']}")

except KeyboardInterrupt:
    print("Shutting down consumer")

finally:
    consumer.close()