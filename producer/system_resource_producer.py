import psutil
import socket
from datetime import datetime, timezone
import config
from kafka import KafkaProducer
import ujson
import platform
import schedule
import time
import sys
import signal


HOSTNAME = socket.gethostname()
HOSTIP = socket.gethostbyname(HOSTNAME)
OSNAME = platform.system()

kafka_addr = f'{config.KAFKA_BROKER_ADDR}:{config.KAFKA_BROKER_PORT}'
producer = KafkaProducer(
    acks='all',
    compression_type='gzip',
    bootstrap_servers=[kafka_addr],
    value_serializer=lambda x: ujson.dumps(x).encode('utf-8')
)


def get_resource_data():
    disk_mount = '/'
    if "window" in OSNAME.lower():
        disk_mount = 'C:\\'
    res_data = {
        "current_time": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S'),
        "os": OSNAME,
        "ip": HOSTIP,
        "hostname": HOSTNAME,
        "cpu_usage_per": psutil.cpu_percent(interval=None),
        "memory_usage_per": psutil.virtual_memory().percent,
        "disk_usage_per": psutil.disk_usage(disk_mount).percent,
        "network_send_kb": int(psutil.net_io_counters().bytes_sent / 1024),
        "network_recv_kb": int(psutil.net_io_counters().bytes_recv / 1024),
    }
    # TODO: get gpu data
    print(res_data)
    # TODO: Send data to Kafka
    # producer.send(topic=config.SYS_RES_TOPIC, value=res_data)
    # producer.flush()


schedule.every(int(config.INTERVAL_TIME)).seconds.do(get_resource_data)

try :
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    producer.flush()
    producer.close()
    sys.exit(0)
