def Data(f):
    data = []
    for line in f:
        data.append(line.strip())
    for line in range(len(data)):
        data[line] = data[line][1:-1]
        data[line] = data[line].split(',')
    return data

def Write(l):
    data=["Province,City,Longitude,Latitude,Distance(km)\n"]
    for line in range(len(l)):
        for item in range(len(l[line])):
            l[line][item] = str(l[line][item])
        data.append(','.join(l[line])+'\n')
    w = open("GeoDistance.csv","w",encoding="UTF-8")
    w.writelines(data)
    w.close()

import numpy as np
r=open("rawdata.csv",encoding='UTF-8')
data=r.readlines()
data=Data(data)
wuhan=[114.31,30.52] #represents the position of wuhan city
for city in range(len(data)):
    #use Haversine formula to calculate the distance https://en.wikipedia.org/wiki/Haversine_formula https://zhuanlan.zhihu.com/p/99338702
    data[city].append(str(2*6378.137*np.arcsin(np.sqrt((np.sin(0.5*(np.deg2rad(float(data[city][3])-wuhan[1]))))**2+np.cos(np.deg2rad(float(data[city][3])))*np.cos(np.deg2rad(wuhan[1]))*(np.sin(0.5*(np.deg2rad(float(data[city][2])-wuhan[0]))))**2))))
Write(data)