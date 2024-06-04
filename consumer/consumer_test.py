from kafka import KafkaConsumer
import json
import config
import traceback


kafka_addr = f'{config.KAFKA_BROKER_ADDR}:{config.KAFKA_BROKER_PORT}'

consumer = KafkaConsumer(
    config.SYS_RES_TOPIC,
    bootstrap_servers=[kafka_addr],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x:json.loads(x.decode('utf-8')),
    consumer_timeout_ms=60000
)

print(f'Start {config.SYS_RES_TOPIC} Consumer')
try:
    for msg in consumer:
        print(f'Topic : {msg.topic}, Partition : {msg.partition}, Offset : {msg.offset}, Key : {msg.key}, value : {msg.value}')
except Exception as e:
    traceback.print_exc()
print('[End] get consumer')