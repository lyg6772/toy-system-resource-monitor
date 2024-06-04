from dotenv import load_dotenv
import os

dotenv_path = f'{os.path.dirname(os.getcwd())}/.env'

load_dotenv(dotenv_path=dotenv_path)

SYS_RES_TOPIC = os.getenv('SYS_RES_TOPIC', '')
KAFKA_BROKER_ADDR = os.getenv('KAFKA_BROKER_ADDR', 'localhost')
KAFKA_BROKER_PORT = os.getenv('KAFKA_BROKER_PORT', 9092)
KAFKA_CONSUMER_PORT = os.getenv('KAFKA_CONSUMER_PORT', 9093)