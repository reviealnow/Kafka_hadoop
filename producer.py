from kafka import KafkaProducer
import json, time

producer = KafkaProducer(
    bootstrap_servers='kafka-0.kafka.default.svc.cluster.local:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(10):
    data = {'device': 'sensor-01', 'temp': 22.5 + i, 'status': 'ok'}
    producer.send('local-topic', data)
    print('Sent:', data)
    time.sleep(1)

producer.close()
