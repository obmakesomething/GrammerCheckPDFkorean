#!/bin/bash

# Run the extract script
python3 extract.py

python3 grammer.py
# Run the extract_connect script
##python3 extract_connect.py
python3 interpret.py
# Run the filter_results script
## python3 filter_results.py
python3 print.py