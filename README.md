Relayr-TestTask
----------
### Features of the Script
- This script uses Python v3.5 as the interpreter
- Following libraries were installed in the virtual environment (venv) for use in the measurements.py Python Script:
  - Pandas -> Software library in Python used for data manipulation and analysis
  - Sys -> This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
  
### Usage of the script
measurements.py action [--device id] [--measurement name] [--start timestamp] [--end timestamp]

The script uses 3 methods to process the data in my_data.csv
- process_dev_data(action, device_id)
  - This method accepts two parameters action and device_id. Both these parameters are passed as command line arguments to the script
