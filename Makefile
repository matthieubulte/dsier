init:
	pip install -r requirements.txt

clean:
	rm data/matrices_ts.npy
	rm data/raw_data.csv
	rm output/*

run:
	./run_analysis.sh

.PHONY: init clean run
