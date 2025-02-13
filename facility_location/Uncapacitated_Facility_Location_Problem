""" UFLP """
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import *

# PARAMETERS
# Creating the random customers
Ncust=20;Ix=[];Iy=[]
for n in range(Ncust):
    Ix.append(round(np.random.uniform(0,100),0))
    Iy.append(round(np.random.uniform(0,100),0))
for n in range(len(Ix)):   print('Customer {}: ({} , {})'.format(n,Ix[n],Iy[n]))  

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

# c[i,j]:Cost of moving one unit of product from i to j 
c={}                                                                           
for i in range(Ncust):
    for j in range(len(Jx)):
        c[i,j]=np.random.randint(1,3)*dist[i,j]

# Fixed Annual Cost 
f={}
for j in range(len(Jx)):
    f[j]=np.random.uniform(1000,10000)


#%% CREATE THE MODEL
m=Model('UFLP')

# Creating the Variables
x={}
for j in J:
    x[j]=m.addVar(vtype=GRB.BINARY, name='x['+str(j)+']')
yvect={}
y={}
for i in I:
    for j in J:
        y[i,j]=m.addVar(vtype=GRB.CONTINUOUS, name='y['+str(i)+','+str(j)+']')

# Creating the Objective Function
m.setObjective(quicksum(f*x[j] for j in J)+quicksum(h[i]*c[i,j]*y[i,j] for i in I for j in J),GRB.MINIMIZE)

#Subject to:
# 1)     
for i in I:
    m.addConstr(quicksum(y[i,j] for j in J)==1)

# 2) A facility can serve a customer if and only if is opened
for i in I:
    for j in J:
        m.addConstr(y[i,j]<=x[j])
        
# 3) Less than 5 miles from NC 
for k in K:
    for j in J:
        m.addConstr(quicksum(o[j,k]>=x[j]))

# 4) Closer than 90 miles from Cust to PotFac
for i in I:
    for j in J:
        m.addConstr(a[j,i]>=x[j])




m.update()
m.optimize() 

#%% Printing the Result

print('\n\n After the optimization the recommendation is that:\n ')
OFx=[]
OFy=[]
for j in J:
    if x[j].x>0.99:
        print('We should open a plant in potential location {}, at coordinates ({})'.format(j,J[j][0],J[j][1]))
        OFx.append(J[j][0])
        OFy.append(J[j][1])

fig, ax=plt.subplots()
ax.scatter(OFx,OFy,marker='.',color='Green',linewidths=30)
ax.scatter(Jx,Jy,marker='x',color='Red',linewidths=20)
ax.scatter(Ix,Iy,marker='o',color='Blue',linewidths=10)





