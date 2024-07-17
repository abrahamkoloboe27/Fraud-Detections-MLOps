#!/bin/bash

# Build Docker image
docker build -t projet_detection_fraudes .

# Run Docker container
docker run -d -p 5000:5000 projet_detection_fraudes
