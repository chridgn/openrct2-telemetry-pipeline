import os

from confluent_kafka import Producer 
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField

from fastapi import FastAPI
from models import Snapshot


BOOTSTRAP_SERVERS=os.environ.get("BOOTSTRAP_SERVERS", "kafka:9092")
LANDING_TOPIC=os.environ.get("LANDING_TOPIC", "telemetry.raw")
SCHEMA_REGISTRY_HOST=os.environ.get("SCHEMA_REGISTRY_HOST", "http://schema-registry:8081")

with open("snapshot.avsc", "r") as f:
    schema_str = f.read()


def produce_message(message: dict):
    kafka_conf = {
        "bootstrap.servers": BOOTSTRAP_SERVERS
    }
    schema_registry_conf = {
        "url": SCHEMA_REGISTRY_HOST
    }

    producer = Producer(kafka_conf)
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    avro_serializer = AvroSerializer(
        schema_registry_client=schema_registry_client,
        schema_str=schema_str
    )

    serialized_value = avro_serializer(message)
    producer.produce(topic=LANDING_TOPIC)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ingest-api is accessible"}

@app.post("/ingest", status_code=202)
async def ingest(data: Snapshot):
    # print(data.model_dump_json(indent=2))
    return {"status": "ok"}

