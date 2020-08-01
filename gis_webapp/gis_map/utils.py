import math

x1= 15.712950725807477
y1= 81.48834228515625
x2= 15.294782590260944
y2= 82.19970703125

distance = [296139.79, 294803.91, 293729.61, 292919.89, 
            292377.07, 292102.78, 292362.59, 292896.22, 
            293697.47, 294764.29] #from vishakhapatanam to datum point

velocity= [[85, 0.03], [110, 0.03], [130, 0.04],
           [140, 0.07], [150, 0.11], [150, 0.14],
           [150, 0.18], [150, 0.24], [145, 0.27], [145, 0.30]] #Total water current


def get_c():
    arr = []
    for k in range(0,10):
        arr.append([(x1+(k/9)*(x2-x1)), (y1+ k*(y2-y1)/9)])
    return arr

def get_time_list():
    time_list = []
    for k in range(0,10):
        time_list.append((distance[k]/72.0222)) #72.0222 is speed of helicopter
    return time_list

def get_displacement():
    displacement = []
    time_list = get_time_list()
    for n in range(0,10):
        displacement.append((time_list[n]*velocity[n][1]))
        displacement[n]=displacement[n]*9.231617281886954e-06
    return displacement

def get_m_list():
    m_list = []
    for n in range(0,10):
        m_list.append((math.tan(math.radians(velocity[n][0]+270))))
    return m_list

def get_centres():
    arr = get_c()
    displacement = get_displacement()
    m_list = get_m_list()
    for n in range(0,10):
        arr[n][0]= arr[n][0]- displacement[n]/math.sqrt(1+ m_list[n]**2)
        arr[n][1]= arr[n][1]- m_list[n]*(displacement[n]/math.sqrt(1+ m_list[n]**2))
    return arr

def get_radius():
    radius = [] # for the smaller circle which will have 50% probability
    time_list = get_time_list()
    for n in range(0,10):
        radius.append(math.sqrt(1852**2 + (0.3*time_list[n])**2 + (1852*0.3)**2))
        radius[n]=radius[n]*9.231617281886954e-06
    return radius

def get_rad3x():
    rad3x =  [] # for the greater circle which will have higher probability
    radius = get_radius()
    for n in range(0,10):
        rad3x.append(radius[n]*3)
    return rad3x

arr = get_centres()
slope= (arr[9][1]-arr[0][1])/(arr[9][0]-arr[0][0])
slope= (-1)/slope # for the slope of the line

def get_polygon():
    radius = get_radius()
    polygon = [] # for the smaller area polygon based on the smaller radius
    polygon.append(arr[0])
    for n in range(0,10):
        polygon.append([(arr[n][0]- radius[n]/math.sqrt(1+ slope**2)),(arr[n][1]- slope*(radius[n]/math.sqrt(1+ slope**2)))])
    polygon.append(arr[9])
    for n in range(0,10):
        polygon.append([(arr[-1*(n+1)][0]+ radius[-1*(n+1)]/math.sqrt(1+ slope**2)),(arr[-1*(n+1)][1]+ slope*(radius[-1*(n+1)]/math.sqrt(1+ slope**2)))])
    polygon.append(arr[0])
    return polygon

def get_polygon3x():
    rad3x = get_rad3x()
    polygon3x = [] # for the larger area polygon based on larger radius
    polygon3x.append(arr[0])
    for n in range(0,10):
        polygon3x.append([(arr[n][0]- rad3x[n]/math.sqrt(1+ slope**2)),(arr[n][1]- slope*(rad3x[n]/math.sqrt(1+ slope**2)))])
    polygon3x.append(arr[9])
    for n in range(0,10):
        polygon3x.append([(arr[-1*(n+1)][0]+ rad3x[-1*(n+1)]/math.sqrt(1+ slope**2)),(arr[-1*(n+1)][1]+ slope*(rad3x[-1*(n+1)]/math.sqrt(1+ slope**2)))])
    polygon3x.append(arr[0])
    return polygon3x
