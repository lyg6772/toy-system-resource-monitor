from kafka import KafkaProducer
import ujson
import traceback

producer = KafkaProducer(
    acks='all',
    compression_type='gzip',
    bootstrap_servers=['146.56.155.146:9092'],
    value_serializer=lambda x: ujson.dumps(x).encode('utf-8')
)

try:
    producer.send('system-resource', value='test_send')
    producer.flush()
    producer.close()
except Exception as e:
    traceback.print_exc()