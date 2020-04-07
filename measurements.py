"""
@author: Sahajhaksh Hariharan
Coded in Python  : v3.5
version = v1.1
"""

import pandas as pd
import sys


global result_dev
global result_meas


def process_dev_data(action, device_id):
    df = pd.read_csv('my_data.csv')
    gf = df.groupby('device_id')
    r = gf.describe()
    my_dict = r.to_dict()

    if action == 'min' and device_id == sys.argv[2]:
        result_dev = my_dict[('measurement_value', 'min')][device_id]
        print("The minimum value of the device is :", result_dev)

    if action == 'max' and device_id == sys.argv[2]:
        result_dev = my_dict[('measurement_value', 'max')][device_id]
        print("The maximum value of the device is :", result_dev)

    if action == 'cnt' and device_id == sys.argv[2]:
        result_dev = my_dict[('measurement_value', 'count')][device_id]
        print("Number of measurements of the device is :", result_dev)

    if action == 'avg' and device_id == sys.argv[2]:
        result_dev = my_dict[('measurement_value', 'mean')][device_id]
        print("Number of average measurements of the device is :", result_dev)


def process_meas_data(action, meas_name):
    global result_meas
    df = pd.read_csv('my_data.csv')
    gf = df.groupby('measurement_name')
    r = gf.describe()
    my_dict = r.to_dict()

    if action == 'min' and meas_name == sys.argv[3]:
        result_meas = my_dict[('measurement_value', 'min')][meas_name]
        print("The minimum value of the measurement name is :", result_meas)

    if action == 'max' and meas_name == sys.argv[3]:
        result_meas = my_dict[('measurement_value', 'max')][meas_name]
        print("The maximum value of the measurement name is :", result_meas)

    if action == 'cnt' and meas_name == sys.argv[3]:
        result_meas = my_dict[('measurement_value', 'count')][meas_name]
        print("Number of measurement type is :", result_meas)

    if action == 'avg' and meas_name == sys.argv[3]:
        result_meas = my_dict[('measurement_value', 'mean')][meas_name]
        print("Average value of the measurement type :", result_meas)


def process_ts_data(action):
    df = pd.read_csv('my_data.csv', parse_dates=['timestamp'])

    if action == 'cnt':
        start_date = sys.argv[4]
        end_date = sys.argv[5]
        after_start_date = df['timestamp'] >= start_date
        before_end_date = df['timestamp'] <= end_date
        between_two_dates = after_start_date & before_end_date
        filtered_values = df.loc[between_two_dates]
        print("The measured values for specified date range are : \n ", filtered_values)


# --------------------#
# Main function call  #
# -----------------  #
def main():
    script = sys.argv[0]
    # print script
    action = sys.argv[1]
    device_id = sys.argv[2]
    meas_name = sys.argv[3]

    # -------------------------------------------------------------------#
    #  Function calls for processing each attribute from the csv file    #
    # -------------------------------------------------------------------#
    process_dev_data(action, device_id)
    process_meas_data(action, meas_name)
    process_ts_data(action)


if __name__ == '__main__':
    main()
