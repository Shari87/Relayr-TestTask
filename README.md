Relayr-TestTask
----------
### Features of the Script
- This script uses Python v3.5 as the interpreter
- Following libraries were installed in the virtual environment (venv) for use in the measurements.py Python Script:
  - Pandas -> Software library in Python used for data manipulation and analysis
  - Sys -> This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
  
Requirement from the task :
measurements.py action [--device id] [--measurement name] [--start timestamp] [--end timestamp]

The script uses 3 methods to process the data in my_data.csv

- process_dev_data(action, device_id)
  - This function accepts two parameters action and device_id. Both these parameters are passed as command line arguments to the function
- process_dev_data(action, meas_name)
  - This function accepts two parameters action and meas_name. Both these parameters are passed as command line arguments to the function
- process_ts_data(action)
  - This function accepts one parameters action. This parameter is passed via command line to the function

Sample output of the program comprising of the inputs from the command line:

measurements.py cnt 0ea7f78a-d224-4d3a-a014-001a0794e746 temperature "2019-05-30 00:00:31.007" "2019-05-30 08:00:51.713"
  - action = cnt
  - --device id = 0ea7f78a-d224-4d3a-a014-001a0794e746
  - --measurement_name = temperature
  - --start_timesamp = "2019-05-30 00:00:31.007"
  - --end_timestamp = "2019-05-30 08:00:51.713"
  
Number of measurements of the device is : 4.0

Number of measurement type is : 4.0

The measured values for specified date range are : 
  - 2  8ac23d27-8747-408f-89d7-c84b827a7776  ...  21.7
  - 6  8ac23d27-8747-408f-89d7-c84b827a7776  ...  21.7

### How to run the script?
  - Clone the repository or download the measurements.py file
  - Run the python script from any editor(PyCharm/Eclipse) or from the commandline with the following parameters:
    - python3 measurements.py cnt 0ea7f78a-d224-4d3a-a014-001a0794e746 temperature "2019-05-30 00:00:31.007" "2019-05-30 08:00:51.713"
