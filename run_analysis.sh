#!/bin/bash

set -e

pip install -r requirements.txt

echo "Running fetch_raw_data.py..."
python src/fetch_raw_data.py

echo "Running prepare_data.py..."
python src/prepare_data.py

echo "Running run_analysis.py..."
python src/run_analysis.py