import rasterio
from rasterio.windows import Window
from rasterio.plot import show
from matplotlib import pyplot as plt
import csv

# open geotif files with data
with rasterio.open('climate_dataset/bio_1(annual_mean_temp).tif') as src:
    annual_mean_temp = src.read()[0]
with rasterio.open('climate_dataset/bio_2(mean_diurnal_range).tif') as src:
    mean_diurnal_range = src.read()[0]
with rasterio.open('climate_dataset/bio_3(isothermality).tif') as src:
    isothermality = src.read()[0]
with rasterio.open('climate_dataset/bio_4(temperature_seasonality).tif') as src:
    temperature_seasonality = src.read()[0]
with rasterio.open('climate_dataset/bio_5(max_temp_warmest_month).tif') as src:
    max_temp_warmest_month = src.read()[0]
with rasterio.open('climate_dataset/bio_6(min_temp_coldest_month).tif') as src:
    min_temp_coldest_month = src.read()[0]
with rasterio.open('climate_dataset/bio_7(temp_annual_range).tif') as src:
    temp_annual_range = src.read()[0]
with rasterio.open('climate_dataset/bio_8(mean_temp_wettest_quarter).tif') as src:
    mean_temp_wettest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_9(mean_temp_driest_quarter).tif') as src:
    mean_temp_driest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_10(mean_temp_warmest_quarter).tif') as src:
    mean_temp_warmest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_11(mean_temp_coldest_quarter).tif') as src:
    mean_temp_coldest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_12(annual_precip).tif') as src:
    annual_precipitation = src.read()[0]
with rasterio.open('climate_dataset/bio_13(precip_wettest_month).tif') as src:
    precipitation_wettest_month = src.read()[0]
with rasterio.open('climate_dataset/bio_14(precip_driest_month).tif') as src:
    precipitation_driest_month = src.read()[0]
with rasterio.open('climate_dataset/bio_15(precip_seasonality).tif') as src:
    precipitation_seasonality = src.read()[0]
with rasterio.open('climate_dataset/bio_16(precip_wettest_quarter).tif') as src:
    precipitation_wettest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_17(precip_driest_quarter).tif') as src:
    precipitation_driest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_18(precip_warmest_quarter).tif') as src:
    precipitation_warmest_quarter = src.read()[0]
with rasterio.open('climate_dataset/bio_19(precip_coldest_quarter).tif') as src:
    precipitation_coldest_quarter = src.read()[0]

# pull from specific geotif file by latitude and longitude
def getval(lon, lat, img):
    idx = src.index(lon, lat)
    return img[idx]

# get all data points from specific location
def pull_values(inputLat, inputLon):
    vals = [
        getval(inputLon,inputLat,annual_mean_temp),
        getval(inputLon,inputLat,mean_diurnal_range),
        getval(inputLon,inputLat,isothermality),
        getval(inputLon,inputLat,temperature_seasonality),
        getval(inputLon,inputLat,max_temp_warmest_month),
        getval(inputLon,inputLat,min_temp_coldest_month),
        getval(inputLon,inputLat,temp_annual_range),
        getval(inputLon,inputLat,mean_temp_wettest_quarter),
        getval(inputLon,inputLat,mean_temp_driest_quarter),
        getval(inputLon,inputLat,mean_temp_warmest_quarter),
        getval(inputLon,inputLat,mean_temp_coldest_quarter),
        getval(inputLon,inputLat,annual_precipitation),
        getval(inputLon,inputLat,precipitation_wettest_month),
        getval(inputLon,inputLat,precipitation_driest_month),
        getval(inputLon,inputLat,precipitation_seasonality),
        getval(inputLon,inputLat,precipitation_wettest_quarter),
        getval(inputLon,inputLat,precipitation_driest_quarter),
        getval(inputLon,inputLat,precipitation_warmest_quarter),
        getval(inputLon,inputLat,precipitation_coldest_quarter),
    ]

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