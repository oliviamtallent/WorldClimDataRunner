import rasterio
from rasterio.windows import Window
from rasterio.plot import show
from matplotlib import pyplot as plt
import csv

data_sets = [
    'climate_dataset/bio_1(annual_mean_temp).tif',
    'climate_dataset/bio_2(mean_diurnal_range).tif',
    'climate_dataset/bio_3(isothermality).tif',
    'climate_dataset/bio_4(temperature_seasonality).tif',
    'climate_dataset/bio_5(max_temp_warmest_month).tif',
    'climate_dataset/bio_6(min_temp_coldest_month).tif',
    'climate_dataset/bio_7(temp_annual_range).tif',
    'climate_dataset/bio_8(mean_temp_wettest_quarter).tif',
    'climate_dataset/bio_9(mean_temp_driest_quarter).tif',
    'climate_dataset/bio_10(mean_temp_warmest_quarter).tif',
    'climate_dataset/bio_11(mean_temp_coldest_quarter).tif',
    'climate_dataset/bio_12(annual_precip).tif',
    'climate_dataset/bio_13(precip_wettest_month).tif',
    'climate_dataset/bio_14(precip_driest_month).tif',
    'climate_dataset/bio_15(precip_seasonality).tif',
    'climate_dataset/bio_16(precip_wettest_quarter).tif',
    'climate_dataset/bio_17(precip_driest_quarter).tif',
    'climate_dataset/bio_18(precip_warmest_quarter).tif',
    'climate_dataset/bio_19(precip_coldest_quarter).tif',
    'climate_dataset/solar_radiation(janurary).tif',
    'climate_dataset/solar_radiation(february).tif',
    'climate_dataset/solar_radiation(march).tif',
    'climate_dataset/solar_radiation(april).tif',
    'climate_dataset/solar_radiation(may).tif',
    'climate_dataset/solar_radiation(june).tif',
    'climate_dataset/solar_radiation(july).tif',
    'climate_dataset/solar_radiation(august).tif',
    'climate_dataset/solar_radiation(september).tif',
    'climate_dataset/solar_radiation(october).tif',
    'climate_dataset/solar_radiation(november).tif',
    'climate_dataset/solar_radiation(december).tif',
    'climate_dataset/water_vapor(janurary).tif',
    'climate_dataset/water_vapor(february).tif',
    'climate_dataset/water_vapor(march).tif',
    'climate_dataset/water_vapor(april).tif',
    'climate_dataset/water_vapor(may).tif',
    'climate_dataset/water_vapor(june).tif',
    'climate_dataset/water_vapor(july).tif',
    'climate_dataset/water_vapor(august).tif',
    'climate_dataset/water_vapor(september).tif',
    'climate_dataset/water_vapor(october).tif',
    'climate_dataset/water_vapor(november).tif',
    'climate_dataset/water_vapor(december).tif',
    'climate_dataset/wind_speed(january).tif',
    'climate_dataset/wind_speed(february).tif',
    'climate_dataset/wind_speed(march).tif',
    'climate_dataset/wind_speed(april).tif',
    'climate_dataset/wind_speed(may).tif',
    'climate_dataset/wind_speed(june).tif',
    'climate_dataset/wind_speed(july).tif',
    'climate_dataset/wind_speed(august).tif',
    'climate_dataset/wind_speed(september).tif',
    'climate_dataset/wind_speed(october).tif',
    'climate_dataset/wind_speed(november).tif',
    'climate_dataset/wind_speed(december).tif',
]

# pull from specific geotif file by latitude and longitude
def getval(lon, lat, img_idx):
    # open geotif files with data
    with rasterio.open(data_sets[img_idx]) as src:
        img = src.read()[0]
    idx = src.index(lon, lat)
    return img[idx]

# get all data points from specific location
def pull_values(inputLat, inputLon):
    vals = []
    for i in range(len(data_sets)):
        vals.append(getval(inputLon, inputLat, i))

    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(vals)

# Example calls with input - (latitude, longitude)
# Tokyo
pull_values(36, 140)
# Delhi
pull_values(29, 76)
# Shanghai
pull_values(31, 121)
# Sao Paulo
pull_values(-24, -47)
# Mexico City
pull_values(20, -99)
# Cairo
pull_values(30, 31)
# Mumbai
pull_values(19, 73)
# Beijing
pull_values(40, 116)
# Dhaka
pull_values(24, 90)
# Osaka
pull_values(35, 136)