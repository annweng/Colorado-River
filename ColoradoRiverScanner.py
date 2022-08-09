from urllib.request import urlopen
import json
import matplotlib.pyplot as plt
import numpy as np
import re

TotalStorage = []

## LAKE POWELL CODE
Powell_json = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/919/json/17.json"
Powell_open = urlopen(Powell_json)
Powell_bytes = Powell_open.read()
Powell_dict = json.loads(Powell_bytes)
Powell_Data = Powell_dict['data']
Powell_Graph_Data = [x for x in Powell_Data if re.search("^2", x[0]) != None]
YearArray = []
PowellVolumeArray = []
for i in Powell_Graph_Data:
    YearArray.append(i[0])
    PowellVolumeArray.append(i[1])
TotalStorage.append(PowellVolumeArray)

## LAKE MEAD CODE
Mead = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/921/json/17.json"
Mead_open = urlopen(Mead).read()
Mead_dict = json.loads(Mead_open)
Mead_Data = Mead_dict['data']
Mead_Graph_Data = [x for x in Mead_Data if re.search("^2", x[0]) != None]
MeadVolumeArray = []
for i in Mead_Graph_Data:
    MeadVolumeArray.append(i[1])
TotalStorage.append(MeadVolumeArray)

## LAKE HAVASU
Havasu = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/923/json/17.json"
Havasu_open = urlopen(Havasu).read()
Havasu_dict = json.loads(Havasu_open)
Havasu_Data = Havasu_dict['data']
Havasu_Graph_Data = [x for x in Havasu_Data if re.search("^2", x[0]) != None]
HavasuVolumeArray = []
for i in Havasu_Graph_Data:
    HavasuVolumeArray.append(i[1])
TotalStorage.append(HavasuVolumeArray)

## LAKE MOHAVE
Mohave = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/922/json/17.json"
Mohave_open = urlopen(Mohave).read()
Mohave_dict = json.loads(Mohave_open)
Mohave_Data = Mohave_dict['data']
Mohave_Graph_Data = [x for x in Mohave_Data if re.search("^2", x[0]) != None]
MohaveVolumeArray = []
for i in Mohave_Graph_Data:
    MohaveVolumeArray.append(i[1])
TotalStorage.append(MohaveVolumeArray)

## NAVAJO RESERVOIR
Navajo = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/920/json/17.json"
Navajo_open = urlopen(Navajo).read()
Navajo_dict = json.loads(Mead_open)
Navajo_Data = Navajo_dict['data']
Navajo_Graph_Data = [x for x in Navajo_Data if re.search("^2", x[0]) != None]
NavajoVolumeArray = []
for i in Navajo_Graph_Data:
    NavajoVolumeArray.append(i[1])
TotalStorage.append(NavajoVolumeArray)

## BLUE MESA RESERVOIR
BlueMesa = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/913/json/17.json"
BlueMesa_open = urlopen(BlueMesa).read()
BlueMesa_dict = json.loads(BlueMesa_open)
BlueMesa_Data = BlueMesa_dict['data']
BlueMesa_Graph_Data = [x for x in BlueMesa_Data if re.search("^2", x[0]) != None]
BlueMesaVolumeArray = []
for i in BlueMesa_Graph_Data:
    BlueMesaVolumeArray.append(i[1])
TotalStorage.append(BlueMesaVolumeArray)

## FLAMING GORGE
FlamingGorge = "https://www.usbr.gov/uc/water/hydrodata/reservoir_data/917/json/17.json"
FlamingGorge_open = urlopen(FlamingGorge).read()
FlamingGorge_dict = json.loads(FlamingGorge_open)
FlamingGorge_Data = FlamingGorge_dict['data']
FlamingGorge_Graph_Data = [x for x in FlamingGorge_Data if re.search("^2", x[0]) != None]
FlamingGorgeVolumeArray = []
for i in FlamingGorge_Graph_Data:
    FlamingGorgeVolumeArray.append(i[1])
TotalStorage.append(FlamingGorgeVolumeArray)

Cumulative_Volume = []
count = 0
while count < len(PowellVolumeArray):
    Daily_Volume = 0
    for lakes in TotalStorage:
        if type(lakes[count]) == float:
            Daily_Volume += lakes[count]
    Cumulative_Volume.append(Daily_Volume)
    count += 1


## GRAPH CODE
plt.title('Colorado River water levels')
plt.xlabel('YEAR')
plt.ylabel('VOLUME (acre feet)')
plt.plot(YearArray, Cumulative_Volume)
plt.savefig("graph.png")
plt.show()

