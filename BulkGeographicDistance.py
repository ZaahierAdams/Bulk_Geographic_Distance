import pandas as pd
from math import sin, cos, sqrt, atan2, radians
import pyproj
import csv
def main():
    df = pd.read_excel('input.xlsx', header =0, index_col = 'id')
    with open('Output_.csv', mode='w') as output:
        writer = csv.writer(output, delimiter=',', lineterminator = '\n')
        writer.writerow(['id',
                         'y1','x1','y2','x2',
                         'd (Haversine formula)','d WGS84',
                         'Foward Azimuth','Back. Azimuth'])
        for index, row in df.iterrows():
            try:
                Lat1 = float(df.loc[index, 'y1']) 
                Lon1 = float(df.loc[index, 'x1']) 
                Lat2 = float(df.loc[index, 'y2']) 
                Lon2 = float(df.loc[index, 'x2']) 
                if pd.isna(Lat2) is True:
                    pass
                else:
                    R = 6373.0
                    lat1 = radians(Lat1)
                    lon1 = radians(Lon1)
                    lat2 = radians(Lat2)
                    lon2 = radians(Lon2) 
                    dlon = lon2 - lon1
                    dlat = lat2 - lat1
                    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))
                    distance_Haversine = R * c
                    geodesic = pyproj.Geod(ellps='WGS84')
                    fwd_azimuth,back_azimuth,distanceWGS84 = geodesic.inv(Lat1, Lon1, Lat2, Lon2)              
                    writer.writerow([index, 
                                     Lat1, Lon1, Lat2, Lon2, 
                                     distance_Haversine*1000, distanceWGS84, 
                                     fwd_azimuth,back_azimuth])       
            except TypeError:
                pass                
if __name__ == '__main__':
    main()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    