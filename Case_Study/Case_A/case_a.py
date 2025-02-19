""" Set Covering Problem """
import numpy as np
from gurobipy import *

#%% PARAMETERS
# Creating the neighborhood locations
# I: is the set of locations we need to serve
I = ['Neighborhood1','Neighborhood2','Neighborhood3','Neighborhood4',
   'Neighborhood5','Neighborhood6','Neighborhood7','Neighborhood8',
   'Neighborhood9','Neighborhood10','Neighborhood11','Neighborhood12',
   'Neighborhood13','Neighborhood14', 'Neighborhood15','Neighborhood16',
   'Neighborhood17','Neighborhood18','Neighborhood19','Neighborhood20', 
   'Neighborhood21','Neighborhood22','Neighborhood23','Neighborhood24',
   'Neighborhood25','Neighborhood26','Neighborhood27','Neighborhood28',
   'Neighborhood29','Neighborhood30','Neighborhood31' ]


coordinate={}                                                # Dictionary that will contain the coordinates
coordinate['Neighborhood1']=[35.9405,-78.89870115]    
coordinate['Neighborhood2']=[36.05952,-78.90548911]  
coordinate['Neighborhood3']=[35.02536,-77.93633527]  
coordinate['Neighborhood4']=[34.91341,-81.461978]   
coordinate['Neighborhood5']=[36.47482,-79.59491191]   
coordinate['Neighborhood6']=[35.36636,-80.10327313]   
coordinate['Neighborhood7']=[36.61737,-76.96518275]  
coordinate['Neighborhood8']=[35.96485,-77.85138376]    
coordinate['Neighborhood9']=[35.3553,-81.07188523]   
coordinate['Neighborhood10']=[35.95009,-78.98072471]  
coordinate['Neighborhood11']=[35.30805,-78.78536946]     
coordinate['Neighborhood12']=[35.41166,-79.56319961]   
coordinate['Neighborhood13']=[36.75454,-78.83257233]   
coordinate['Neighborhood14']=[36.46565,-78.95642837]  
coordinate['Neighborhood15']=[35.17293,-78.85543841]   
coordinate['Neighborhood16']=[36.73573,-79.58559494]  
coordinate['Neighborhood17']=[35.88996,-80.65308117]  
coordinate['Neighborhood18']=[36.35274,-78.71235081]  
coordinate['Neighborhood19']=[36.39771,-76.27821844]  
coordinate['Neighborhood20']=[35.45436,-79.49948708]  
coordinate['Neighborhood21']=[36.60613,-79.89409166]    
coordinate['Neighborhood22']=[35.47372,-77.79994467]  
coordinate['Neighborhood23']=[35.87726,-77.05774268]  
coordinate['Neighborhood24']=[36.17111,-76.58442876]  
coordinate['Neighborhood25']=[37.49959,-78.63937056]  
coordinate['Neighborhood26']=[36.62883,-77.7553535]  
coordinate['Neighborhood27']=[35.06429,-78.91134421]  
coordinate['Neighborhood28']=[34.90717,-78.29861561]  
coordinate['Neighborhood29']=[34.94897,-78.82959221]  
coordinate['Neighborhood30']=[35.42296,-79.05687759]  
coordinate['Neighborhood31']=[36.49349,-79.22128678]  

#%% Set covering distance
# K: Is the set of different drone types.
K = ['I', 'II', 'III']
'''
I:   IRQN-2B / Covers 5 Miles / Costs $5,000.00$
II:  PELJC-TYE2 / Covers 10 Miles / Costs $50,000.00$
III: CAZD-OR3000 / Covers 50 Miles / Costs $100,000.00$
'''

d_coverage = {}
d_coverage['I'] = [5]
d_coverage['II'] = [10]
d_coverage['III'] = [50]

d_cost = {}
d_cost['I'] = [10000]
d_cost['II'] = [50000]
d_cost['III'] = [100000]


    
# Creating the potential locations for the charging stations 
# J is the set of potential locations to install charging stations, wich completely coincide with I.

J = I.copy()

#Define Great Circle Distance Function (with not circulaity factor)

def greatCircleDistance(point1,point2,circuityFactor=1):   
    lat1=point1[0]*2*np.pi/360                   # Changing the latitud from Degrees to radians                 
    lat2=point2[0]*2*np.pi/360
    deltaLatitud=(point1[0]-point2[0])/2         # Changing the latitud from Degrees to radians
    deltaLongitud=(point1[1]-point2[1])/2        # Changing the latitud from Degrees to radians
    deltaLatitudRad=deltaLatitud*2*np.pi/360     # Changing the latitud from Degrees to radians
    deltaLongitudRad=deltaLongitud*2*np.pi/360   # Changing the latitud from Degrees to radians
    r=3958.8
    innergcd=np.sqrt((np.sin(deltaLatitudRad)**2)+np.cos(lat1)*np.cos(lat2)*(np.sin(deltaLongitudRad)**2))
    gcd=round(2*r*np.arcsin(innergcd),2)*circuityFactor   
    return gcd

# Great Circle Distance Parameter
dist={}
for i in I:
    for j in J:
        dist[i,j]= greatCircleDistance(coordinate[i], coordinate[j], 1) #Great Circle Distance

# Covering binary variable
# Becomes 1 if a charging station in location j of drone type k covers location i 
a={}
for i in I: 
    for j in J:
        for k in K:
            if dist[i,j]<d_coverage[k]:
                a[i,j,k]=1
            else:
                a[i,j,k]=0
        

#%% Part a, b
# We take into account only one type of drone that covers 5 miles
K=['I']
#% Create Model
m=Model('SetCovering')

# Creating the Variables
x={}
# Becomes 1 if we place a charging station from a drone type k at location j
for j in J:
    for k in K:
        x[j,k]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+'-'+str(k)+']')


# Creating the Objective Function
# We want to minimize the total cost of placing charging stations
m.setObjective(quicksum(x[j,k]*d_cost[k][0] for j in J for k in K),GRB.MINIMIZE)


#Subject to:
# 1) Each location i must be covered by at least one charging station.    
for i in I:
    m.addConstr(quicksum(a[i,j,k]*x[j,k] for j in J for k in K)>=1) 

# 2) At each neighborhood we can only place one type of drone.
for j in J:
    m.addConstr(quicksum(x[j,k] for k in K)<=2) 


m.update()
m.optimize() 

#%% Results a and b
# Answer a)
count=0
count_I=0
count_II=0
count_III=0
list_opens=[]

for j in J:
    for k in K:
        if x[j,k].x>.99:
            count+=1
            list_opens.append('{}, at coordinates ({}) of type {}'.format(j, coordinate[j],k))
            if k=='I':
                count_I+=1
            # elif k=='II':
            #     count_II+=1
            # elif k=='III':
            #     count_III+=1
            # else:
            #     print('ERROR')
                
print('\n\n Answer of part a):\n')           
print(f'We need to install {count} charging facilities')
print(f' {count_I} of Type I')
# print(f' {count_II} of Type II')
# print(f' {count_III} of Type III\n')

print('\nIn locations:\n')
for n in list_opens:
    print(n)

#%% Answer b)
covers_at_location={}
for i in I:
    covers=0
    for j in J:
        for k in K:
            if x[j,k].x*a[i,j,k]==1:
                covers+=1
    covers_at_location[i]=covers

more_than_one_cover=0
more_than_one_cover_list=[]
for n in covers_at_location:
    if covers_at_location[n]>1:
        more_than_one_cover_list.append()
        more_than_one_cover+=1

print(f'In this setting {more_than_one_cover} locations are cover by more than a drone.')

if more_than_one_cover>1:
    for n in more_than_one_cover_list:
        print(f' {n} is covered {covers_at_location[n]} times ')

#%% Part c) Here we want to know if it is posible to cover all locations with two charging stations.
# We keep the constraint that forces us to have only one charging stations at each neighborhood.

# Let l be the number drones we want to be covering at each location:
l=2
# l=3
# l=4

#% Create Model
m.close()
m=Model('SetCovering_c')

# Creating the Variables
x={}
# Becomes 1 if we place a charging station from a drone type k at location j
for j in J:
    for k in K:
        x[j,k]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+'-'+str(k)+']')


# Creating the Objective Function
# We want to minimize the total cost of placing charging stations
m.setObjective(quicksum(x[j,k]*d_cost[k][0] for j in J for k in K),GRB.MINIMIZE)


#Subject to:
# 1) Each location i must be covered by at least one charging station.    
for i in I:
    m.addConstr(quicksum(a[i,j,k]*x[j,k] for j in J for k in K)>=l) 

# 2) At each neighborhood we can only place one type of drone.
for j in J:
    m.addConstr(quicksum(x[j,k] for k in K)<=1) 


m.update()
m.optimize() 

if m.status==2:
    print('Model is Feasible')
    count=0
    count_I=0
    count_II=0
    count_III=0
    list_opens=[]

    for j in J:
        for k in K:
            if x[j,k].x>.99:
                count+=1
                list_opens.append('{}, at coordinates ({}) of type {}'.format(j, coordinate[j],k))
                if k=='I':
                    count_I+=1
                elif k=='II':
                    count_II+=1
                elif k=='III':
                    count_III+=1
                else:
                    print('ERROR')
                    
    print('\n\n Answer of part a):\n')           
    print(f'We need to install {count} charging facilities')
    print(f' {count_I} of Type I')
    print(f' {count_II} of Type II')
    print(f' {count_III} of Type III\n')

    print('\nIn locations:\n')
    for n in list_opens:
        print(n)
elif m.Status==3:
    print('\n\n Model is not feasible')
    print(f'with the current setting it is not posible to cover {l} times each location ')
    
#%% f) Here we can add other types of drones
K = ['I', 'II', 'III']     
l=1
# l=2
# l=3

#% Create Model
m.close()
m=Model('SetCovering_c')

# Creating the Variables
x={}
# Becomes 1 if we place a charging station from a drone type k at location j
for j in J:
    for k in K:
        x[j,k]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+'-'+str(k)+']')


# Creating the Objective Function
# We want to minimize the total cost of placing charging stations
m.setObjective(quicksum(x[j,k]*d_cost[k][0] for j in J for k in K),GRB.MINIMIZE)


#Subject to:
# 1) Each location i must be covered by at least one charging station.    
for i in I:
    m.addConstr(quicksum(a[i,j,k]*x[j,k] for j in J for k in K)>=l) 

# 2) At each neighborhood we can only place one type of drone.
for j in J:
    m.addConstr(quicksum(x[j,k] for k in K)<=1) 


m.update()
m.optimize() 

if m.status==2:
    print('Model is Feasible')
    count=0
    count_I=0
    count_II=0
    count_III=0
    list_opens=[]

    for j in J:
        for k in K:
            if x[j,k].x>.99:
                count+=1
                list_opens.append('{}, at coordinates ({}) of type {}'.format(j, coordinate[j],k))
                if k=='I':
                    count_I+=1
                elif k=='II':
                    count_II+=1
                elif k=='III':
                    count_III+=1
                else:
                    print('ERROR')
                    
    print('\n\n Answer of part a):\n')           
    print(f'We need to install {count} charging facilities')
    print(f' {count_I} of Type I')
    print(f' {count_II} of Type II')
    print(f' {count_III} of Type III\n')

    print('\nIn locations:\n')
    for n in list_opens:
        print(n)
        
elif m.Status==3:
    print('\n\n Model is Feasible')
    print(f'with the current setting it is not posible to cover {l} times each location ')





