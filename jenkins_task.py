#!/usr/bin/python3

"""
Jenkins task as a python script
"""

from datetime import datetime
from time import sleep

channel_dict = {}

def create_channel(channel_type,channel_number):
    print("Creating Channel...")
    sleep(3)
    print("status: 10% complete")
    sleep(3)
    print("status...")
    sleep(3)
    channel_dict['type'] = "PPV"
    channel_dict['number'] = 4
    return channel_dict



if __name__ == "__main__":

    # mocked input
    channel_type = "F1"
    channel_number = "4"

    new_channel = create_channel("PPV",4)

    print(f"channel {new_channel['type']} {new_channel['number']} has completed ")

    
    
