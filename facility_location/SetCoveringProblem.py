""" Set Covering Problem """
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *

# PARAMETERS
# Creating the random customers
Ncust=15;Ix=[];Iy=[]
for n in range(Ncust):
    Ix.append(round(np.random.uniform(0,100),0))
    Iy.append(round(np.random.uniform(0,100),0))
for n in range(len(Ix)):   print('Customer {}: ({} , {})'.format(n,Ix[n],Iy[n]))  

cover_dist=2000

# Demand (hi)
h={}
for i in range(Ncust):
    h[i]=round(np.random.rand()*1000000,2)  
    
# Creating the random potential facilities
Jx=Ix[:int(round(Ncust*.45,0))].copy()
Jy=Iy[:int(round(Ncust*.45,0))].copy()
for n in range(len(Jy)):
    Jx.append(round((np.random.uniform(30,70)),0))
    Jy.append(round((np.random.uniform(30,70)),0))
for n in range(len(Jx)):   print('PotentialFacility {}: ({} , {})'.format(n,Jx[n],Jy[n]))    

fig, ax=plt.subplots()

ax.scatter(Jx,Jy,marker='x',color='Red',linewidths=20)
ax.scatter(Ix,Iy,marker='o',color='Blue',linewidths=10)


# Distances as Parameters
dist={}
for i in range(Ncust):
    for j in range(len(Jx)):
        dist[i,j]=np.sqrt(((Ix[i]-Jx[j])**2)+((Iy[i]-Jy[j])**2))

# Binary Covering variable
a={}
for i in range(Ncust):
    for j in range(len(Jx)):
        if dist[i,j]<cover_dist:
            a[i,j]=1
        else:
            a[i,j]=0
            
            

# Fixed Annual Cost 
f={}
for j in range(len(Jx)):
    f[j]=np.random.uniform(1000,10000)


#%% CREATE THE MODEL
m=Model('SetCovering')

# Creating the Variables
x={}
for j in range(len(Jx)):
    x[j]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+']')


# Creating the Objective Function
m.setObjective(quicksum(f[j]*x[j] for j in range(len(Jx))),GRB.MINIMIZE)

#Subject to:
# 1)     
for i in range(Ncust):
    m.addConstr(quicksum(a[i,j]*x[j] for j in range(len(Jx)))>=1)


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
ax.scatter(OFx,OFy,marker='.',color='Green',linewidths=30)
ax.scatter(Jx,Jy,marker='x',color='Red',linewidths=20)
ax.scatter(Ix,Iy,marker='o',color='Blue',linewidths=10)






