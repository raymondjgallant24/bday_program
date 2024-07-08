import xarray as xr
import numpy as np
import pandas as pd
import matplotlib as mpl 
import time
import random
import datetime

def gen_rand_bday():
    #Create date range
    start_date = datetime.date(2013, 1, 1)
    end_date = datetime.date(2014, 12, 31)
#How many days in dataset?: 729 
    delta = end_date - start_date
    total_days = delta.days 
    random_days = random.randint(0, total_days)

#Add random number of days to start_date
    random_date = start_date +datetime.timedelta(days = random_days)
#Format to mm/dd/yyyy 
    formatted_date = random_date.strftime("%m/%d/%Y")
    return formatted_date


def gen_lat_values():
    test_lat = random.uniform(-90, 90)
    return test_lat

def gen_lon_values():
    test_lon = random.uniform(-180, 180)
    return test_lon

def gen_test_case():
    test_case = {
            "name": "Testing",
            "birthday": gen_rand_bday(),
            "lat": gen_lat_values(),
            "lon": gen_lon_values()
        }
    return test_case 


def create_mass_cases(cases):
    mass_cases = []
    for c in range(cases):
        n = gen_test_case()
        mass_cases.append(n)
    print(mass_cases)
    return mass_cases
    
create_mass_cases(10)
