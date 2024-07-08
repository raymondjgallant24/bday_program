import xarray as xr
import numpy as np
import pandas as pd
import time
import random
import datetime

def gen_rand_bday():
    start_date = datetime.date(2013, 1, 1)
    end_date = datetime.date(2014, 12, 31)
    delta = end_date - start_date
    total_days = delta.days
    random_days = random.randint(0, total_days)
    random_date = start_date + datetime.timedelta(days=random_days)
    formatted_date = random_date.strftime("%m/%d/%Y")
    return formatted_date

def gen_lat_values():
    return random.uniform(-90, 90)

def gen_lon_values():
    return random.uniform(-180, 180)

def gen_test_case(test_lat, test_lon, test_bday):
    test_case = {
        "name": "Testing",
        "birthday": test_bday,
        "lat": test_lat,
        "lon": test_lon
    }
    return test_case 

def gen_mass_cases(cases):
    mass_cases = []
    for _ in range(cases):
        test_lat = gen_lat_values()
        test_lon = gen_lon_values()
        test_bday = gen_rand_bday()
        test_case = gen_test_case(test_lat, test_lon, test_bday)
        mass_cases.append(test_case)
    return mass_cases

def load_dataset():
    ds = xr.tutorial.load_dataset("air_temperature")
    return ds

def get_birthday_temp(ds, test_case):
    date = pd.to_datetime(test_case['birthday'])
    temp_at_location = ds.sel(lat=float(test_case['lat']), lon=float(test_case['lon']), method='nearest')
    temp_on_date = temp_at_location.sel(time=date, method='nearest')
    air_temp = temp_on_date['air'].item()
    air_temp = (air_temp - 273.15) * 1.8 + 32
    return air_temp

def main():
    cases = 1000
    test_cases = gen_mass_cases(cases)
    ds = load_dataset()
    total_time = 0

    for test_case in test_cases:
        start_time = time.time()
        air_temp = get_birthday_temp(ds, test_case)
        end_time = time.time()
        total_time += end_time - start_time

        print(f"The average air temperature on {test_case['name']}'s birthday ({test_case['birthday']}) at the location of ({test_case['lat']}, {test_case['lon']}) was {air_temp:.2f} degrees Fahrenheit.")

    avg_time = total_time / cases
    print(f" The average execution time over {cases} cases is {avg_time:.10f} seconds")

if __name__ == "__main__":
    main()
