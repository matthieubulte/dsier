# Correlation of major EU economies' stock indices

This repository contains the code for reproducing the results of my submission to the DSIER class. Here, I study the correlation between the major stock indices of the 10 largest EU economies (measured in terms of GDP, source: [wikipedia](https://en.wikipedia.org/wiki/List_of_sovereign_states_in_Europe_by_GDP_(nominal))).

The list of countries and indices can be found under `data/indices.csv`. Due to data scarcity, Poland (ranked #6) removed due to data scarcity and the 11th largest economy, Austria, was instead chosen to replace it.

## Requirements

- Python 3.9.16
- Dependencies can be found in `requirements.txt` and installed with `pip install -r requirements.txt` in your environment

## Running the analysis

To reproduce the results used in the final presentation, you can run the following scripts in the order in which they are presented:
1. `src/fetch_raw_data.py` will fetch the raw data from yahoo finance into `data/raw_data.csv`
2. `src/prepare_data.py` will transform the raw yahoo finance data into a monthly time series of correlation matrices saved in `data/matrices_ts.npy`
3. `src/run_analysis.py` will run the statistical method and put related plots in `output/`.
Alternatively, you can just run `make` which will install dependencies and run the scripts.