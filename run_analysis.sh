#!/bin/bash

set -e

pip install -r requirements.txt

echo "Running fetch_raw_data.py..."
python fetch_raw_data.py

echo "Running prepare_data.py..."
python prepare_data.py

