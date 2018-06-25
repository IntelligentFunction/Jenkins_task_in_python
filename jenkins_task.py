#!/usr/bin/python3

"""
Jenkins task as a python script
"""

from datetime import datetime
from time import sleep

channel_dict = {}

def create_channel(channel_type,channel_number):
    print("Creating Channel...")
    sleep(10)
    print("status: 10% complete")
    sleep(10)
    print("status...")
    sleep(10)
    channel_dict['type'] = channel_type
    channel_dict['number'] = channel_number
    channel_dict['timestamp'] = datetime.now()
    return channel_dict



if __name__ == "__main__":

    # mocked input
    from random import choice
    channel_type = ['EFL','PPV','F1']
    channel_number = [i for i in range(1,12)]

    type_choice = choice(channel_type)
    number_choice = choice(channel_number)

    new_channel = create_channel(type_choice,number_choice)
    print(f"\n\t Channel {new_channel['type']}, {new_channel['number']} has completed \n\t at {new_channel['timestamp']} ")

    
    
