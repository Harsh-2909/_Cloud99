import math

def cal(LKP, speed, altitude, direction):
    search = [22.806567100271522, 86.19873046875]
    LKP = list(map(float, LKP))
    speed = float(speed) # input in m/sec
    altitude = float(altitude) # input in metres
    g = 9.76318 #acceleration due to gravity
    rf = 9.231617281886954e-06

    fall_time= math.sqrt((2*altitude)/g)
    d = speed*fall_time*rf # horizontal displacement
    m = math.tan(90-direction)
    if direction==0 or direction==360:
        LKP[1]=LKP[1]+d
    elif direction == 180:
        LKP[1]=LKP[1]-d
    elif direction == 90:
        LKP[0]=LKP[0]+d
    elif direction == 270:
        LKP[0]=LKP[0]-d
    elif direction>0 and direction<180:
        LKP[0]=LKP[0]+ d/(math.sqrt(1+ m**2))
        LKP[1]=LKP[1]+ m*d/(math.sqrt(1+ m**2))
    elif direction>180 and direction<359.99999999:
        LKP[0]=LKP[0]- d/(math.sqrt(1+ m**2))
        LKP[1]=LKP[1]- m*d/(math.sqrt(1+ m**2))
    nav_err = 1852 # navigational fix error of Military Radar
    dr_perc = 0.05 # Dead reckoning % for aircraft with more than 2 engine
    dr_distance = speed*fall_time
    dr_err = dr_perc*dr_distance
    dist = (math.sqrt((search[1]-LKP[1])**2 + (search[0]-LKP[0])**2))/rf
    search_err = 5*1852 + 0.05*float(dist) # search facility error
    radius = math.sqrt((nav_err+float(dr_err))**2 +search_err**2)
    return LKP, radius, radius*3 # shifted LKP is the center, 50% radius, 100% radius