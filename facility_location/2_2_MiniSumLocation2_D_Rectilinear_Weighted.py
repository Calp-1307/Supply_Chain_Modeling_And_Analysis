# -*- coding: utf-8 -*-
"""
Minisum Location Problem 2D-Rectilinear Class Example @author: carlo
"""
#Importing the necessary packages 
import scipy                                                                   # Scipy to optimize
from scipy import optimize                                                     # From scipy the optimization package
import numpy as np                                                             # Numpy to make the computations (in matrix form)
import matplotlib.pyplot as plt                                                # Package to plot

scale=15                                                                       # A constant thta amplifies the random coodinates                          
linewiths=40                                                                    # Constante that sets the size of the lines in the plots
# The next three commneted lines can be uncommented if you want to generate Ncust number of random customers 
#Ncust=5                                                                       # Number of Customers
#I=np.random.rand(Ncust,2)*scale                                               # Random Coordinates
#W=np.random.rand(Ncust,1)*scale                                               # Random Weighted demand

I=np.array([(1,3),(7,1),(3,7),(12,5),(10,8.5)])                                # Class example coordinate
W=np.array([600,200,400,200,1000])                                             # Class example weighted demand
for n in range(len(I)):   print('Customer {}: ({} , {})'.format(n,I[n][0],I[n][1])) # Print     

#% Decalring the points of the margins
marginUpperx=[0, scale]
marginUppery=[scale, scale]
marginLowerx=[0, scale] 
marginLowery=[0, 0]
marginLeftx=[scale, scale]
marginLefty=[0, scale]
marginRightx=[0, 0]
marginRighty=[0., scale]

fig, ax=plt.subplots()                                                          # Creating the figure of the 1st plot 
ax.plot(marginUpperx,marginUppery,color='Green')                                # Plotting the upper margin
ax.plot(marginLowerx,marginLowery,color='Green')                                # Plotting the lower margin 
ax.plot(marginLeftx,marginLefty,color='Green')                                  # Plotting the left margin 
ax.plot(marginRightx,marginRighty,color='Green')                                # Potting the right margin
ax.scatter(I[:,0],I[:,1],marker='.',color='Blue',linewidths=linewiths)          # Plotting the customer coordinates

# This loop is to print the label (demand) on each of the coordinate 
for i, txt in enumerate(W): 
    ax.annotate(txt, (I[i][0], I[i][1]),fontsize=50)
    
    
    
distRectilinear = lambda X: np.sum((W*(np.sum(np.abs(I-X),axis=1))),0)          # Lambda function (weighted rectilinear distance) 
X0=np.array([1,1])                                                              # Initial point for the nonlinear optimization 
xopt = scipy.optimize.minimize(distRectilinear,X0,method='BFGS')                # Optimization command using ('BFGS') 
print('\n Optimal location BFGS: {}'.format(xopt.x))                            # Printing the coordiantes in the Console
ax.scatter(xopt.x[0],xopt.x[1],marker='x',color='Red',linewidths=linewiths*.2)  # Plotting the coordinates in the figure
plt.title('Single Mini-Sum Facility location Using BFGS')                       # Printing the title on the figure


fig, ax=plt.subplots()                                                          # Creating the figure of the 1st plot 
ax.plot(marginUpperx,marginUppery,color='Green')                                # Plotting the upper margin
ax.plot(marginLowerx,marginLowery,color='Green')                                # Plotting the lower margin 
ax.plot(marginLeftx,marginLefty,color='Green')                                  # Plotting the left margin 
ax.plot(marginRightx,marginRighty,color='Green')                                # Potting the right margin
ax.scatter(I[:,0],I[:,1],marker='.',color='Blue',linewidths=linewiths)          # Plotting the customer coordinates
# This loop is to print the label (demand) on each of the coordinate 
for i, txt in enumerate(W):
    ax.annotate(txt, (I[i][0], I[i][1]))
    
distRectilinear = lambda X: np.sum((W*(np.sum(np.abs(I-X),axis=1))),0)          # Lambda function (rectilinear distance) 
X0=np.array([1,1])                                                              # Initial point for the nonlinear optimization 
xopt = scipy.optimize.minimize(distRectilinear,X0,method='Nelder-Mead')         # Optimization command using ('Nelder-Mead') 
print('\n Optimal location Nelder-Mead: {}'.format(xopt.x))                     # Printing the coordiantes in the Console
ax.scatter(xopt.x[0],xopt.x[1],marker='x',color='Red',linewidths=linewiths*.2)  # Plotting the coordinates in the figure
plt.title('Single Mini-Sum Facility location Using Nelder-Mead')                # Printing the title on the figure






