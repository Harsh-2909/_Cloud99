import math

rf=9.231617281886954e-06
def distMeasure(a,b):
    dlat= math.radians(a[0])-math.radians(b[0])
    dlon= math.radians(a[1])-math.radians(b[1])
    return 6371*2*(math.asin(math.sqrt(math.sin(dlat / 2)**2 + math.cos(math.radians(a[0])) * math.cos(math.radians(b[0])) * math.sin(dlon / 2)**2)))

def cal(LKP, speed, altitude, direction, endurance):
    lat_d, lat_m, lat_s = map(int, LKP[0].split("."))
    lon_d, lon_m, lon_s = map(int, LKP[1].split("."))

    north = False if lat_d < 0 else True
    east = False if lon_d < 0 else True

    LKP=[abs(lat_d)+lat_m*0.016667+lat_s*0.00027778, abs(lon_d)+lon_m*0.016667+lon_s*0.00027778]

    if not north:
        LKP[0] = (-1) * LKP[0]
    if not east:
        LKP[1] = (-1)*LKP[1]

    speed= float(speed) * 0.514444 #input 388.769 knots converted to m/s using conv. factor
    altitude= float(altitude) * 1852 #input 23NM converted to metre
    endurance= float(endurance) * 3600 #input in hour convert to sec

    m = math.tan(math.radians(90-direction))
    m1=math.tan(math.radians(90-(direction+10)))
    m2=math.tan(math.radians(90-(direction-10)))
    k=0
    if direction>0 and direction<90:
        k=1
    elif direction>90 and direction<180:
        k=-1
    elif direction>180 and direction<270:
        k=-1
    elif direction>270 and direction<359.9999999:
        k=1

    Radius = speed*endurance

    search_list= [[9.958135,76.251352, 'Kochi', '9595965255'], [12.845297,74.844182, 'Mangalore', '9878456512'],
                [19.076742,72.822744,'Mumbai', '6568696362'], [22.779764,69.676952, 'Gujarat','5256545859'],
                [21.691194, 87.736080, 'Mandarmani', '8484858289'], [17.727242, 83.343863, 'Vishakhapatnam', '4241415788'], 
                [13.088354,80.298761,'Chennai', '4543432116'], [8.092543, 77.555034, 'Kanyakumari', '7878744129']]
    dist_list=list()

    for n in range(0,8):
        dist_list.append(distMeasure(LKP, [search_list[n][0], search_list[n][1]]))

    sector = list()
    polygon = list()
    slope=-1/m
    rad= Radius*rf*k
    line_datum= [LKP, [LKP[0]+rad/math.sqrt(1+m**2), LKP[1]+m*rad/math.sqrt(1+m**2)]]

    rad= 5*1852*rf
    polygon.append(line_datum[0])
    for n in range(0,len(line_datum)):
        polygon.append([(line_datum[n][0]- rad/math.sqrt(1+ slope**2)), (line_datum[n][1]- slope*(rad/math.sqrt(1+ slope**2)))])
    polygon.append(line_datum[-1])
    for n in range(0,len(line_datum)):
        polygon.append([(line_datum[-1*(n+1)][0]+ rad/math.sqrt(1+ slope**2)),(line_datum[-1*(n+1)][1]+ slope*(rad/math.sqrt(1+ slope**2)))])
    polygon.append(line_datum[0])

    rad= Radius*rf*k
    sector.append(LKP)
    sector.append([LKP[0]+rad/math.sqrt(1+m1**2), LKP[1]+m1*rad/math.sqrt(1+m1**2)])
    sector.append([LKP[0]+rad/math.sqrt(1+m2**2), LKP[1]+m2*rad/math.sqrt(1+m2**2)])
    sector.append(LKP)

    return LKP, Radius, polygon, sector, search_list[dist_list.index(min(dist_list))]