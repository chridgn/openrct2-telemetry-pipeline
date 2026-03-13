#!/bin/bash

set -e

KAFKA=/opt/kafka/bin/kafka-topics.sh
BS=kafka:9092

$KAFKA --bootstrap-server $BS --create --if-not-exists \
  --topic telemetry.raw --partitions 3 \
  --config retention.ms=-1

