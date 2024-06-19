from kafka import KafkaProducer
import ujson
import traceback
import config

kafka_addr = f'{config.KAFKA_BROKER_ADDR}:{config.KAFKA_BROKER_PORT}'
producer = KafkaProducer(
    acks='all',
    compression_type='gzip',
    bootstrap_servers=[kafka_addr],
    value_serializer=lambda x: ujson.dumps(x).encode('utf-8')
)
print('Kafka Producer Start')
try:
    producer.send(topic=config.SYS_RES_TOPIC, value='test_send')
    producer.flush()
    producer.close()
except Exception as e:
    traceback.print_exc()

print('Kafka Producer End')