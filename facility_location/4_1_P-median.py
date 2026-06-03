""" p-Median Facility Location Problem """
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *

# PARAMETERS
p=4
# Creating the random customers
Ncust=20;Ix=[];Iy=[]

for n in range(Ncust):
    Ix.append(round(np.random.uniform(0,100),0))
    Iy.append(round(np.random.uniform(0,100),0))  
print('\n Customers \n')
for n in range(len(Ix)):   print('Customer {}: ({} , {})'.format(n,Ix[n],Iy[n]))  
#%
# Demand (hi)
h={}
for i in range(Ncust):
    h[i]=round(np.random.rand()*1000000,2)      
   
#%%
for i in range(Ncust):
    print('Demand Customer {}: {}'.format(i,h[i]))    
   
    
   
#%% Creating the random potential facilities
Jx=Ix[:int(round(Ncust*.3,0))].copy()
Jy=Iy[:int(round(Ncust*.3,0))].copy()
NPotFac=len(Jx)
for n in range(NPotFac):
    Jx.append(round((np.random.uniform(30,70)),0))
    Jy.append(round((np.random.uniform(30,70)),0))

print('\n\n Potential Facilitites\n')
for n in range(len(Jx)):   print('PotentialFacility {}: ({} , {})'.format(n,Jx[n],Jy[n]))    


fig, ax=plt.subplots()
ax.scatter(Jx,Jy,marker='x',color='Red',linewidths=20,label='PotentialFacility')
ax.scatter(Ix,Iy,marker='o',color='Blue',linewidths=7,label='Customer')
ax.legend()


#%% Distances as Parameters
dist={}
for i in range(Ncust):
    for j in range(len(Jx)):
        dist[i,j]=np.sqrt(((Ix[i]-Jx[j])**2)+((Iy[i]-Jy[j])**2))


# c[i,j]:Cost of moving one unit of product from i to j 
c={}                                                                           
for i in range(Ncust):
    for j in range(len(Jx)):
        c[i,j]=np.random.randint(1,3)*dist[i,j]








#%% CREATE THE MODEL
print('\n\n Initiallization of the Model \n')
m=Model('P-median Problem')

# Creating the Variables
x={}
for j in range(len(Jx)):
    x[j]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+']')

y={}
for i in range(Ncust):
    for j in range(len(Jx)):
        y[i,j]=m.addVar(vtype=GRB.CONTINUOUS, name='y['+str(i)+','+str(j)+']')



# Creating the Objective Function
m.setObjective(quicksum(h[i]*c[i,j]*y[i,j] for i in range(Ncust) for j in range(len(Jx))),\
               GRB.MINIMIZE)

#Subject to:
# 1) All the customer demands must be fulfilled. 
for i in range(Ncust):
    m.addConstr(quicksum(y[i,j] for j in range(len(Jx)))==1)

# 2) If the facility is not open, it cannot serve any customer
for i in range(Ncust):
    for j in range(len(Jx)):
        m.addConstr(y[i,j]<=x[j])

# 3) We must open "p" facilities         
m.addConstr(quicksum(x[j] for j in range(len(Jx)))==p)  


m.update()
m.optimize() 


#%% Printing the Result
print('\n\n After the optimization the recommendation is that:\n ')
OFx=[]
OFy=[]

for j in range(len(Jx)):
    if x[j].x>.99:
        print('We should open a plant in potential location {}, at coordinates ({},{})'.format(j,Jx[j],Jy[j]))
        OFx.append(Jx[j])
        OFy.append(Jy[j])

fig, ax=plt.subplots()
ax.scatter(OFx,OFy,marker='.',color='Green',linewidths=25, label='Opened Facility')
ax.scatter(Jx,Jy,marker='x',color='Red',linewidths=20,label='PotentialFacility')
ax.scatter(Ix,Iy,marker='.',color='Blue',linewidths=5,label='Customer')
ax.legend()

