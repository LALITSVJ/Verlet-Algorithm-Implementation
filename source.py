# My 1st ever assignment project
# Implementation of Verlet algorithm
# Problem Statement: A container is filled with an inert gas having 'n' number of molecules. Task is to find the position and velocity of those molecules after time interval 't' using Verlet algorithm. Print the position and velocity matrices and plot position and velocity graphs.

import numpy as np
import matplotlib.pyplot as plt
import math

print('Mention the coordinates of molecules: ')
X = (input('\nMention the X coordinates: '))
Y = (input('\nMention the Y coordinates: '))

X = [int(x) for x in X.split()]
Y = [int(y) for y in Y.split()]

print('X= ',X)
print('\nY= ',Y)

# Particles position matrix at t=0 sec
c0matrix = []
for i in X:
    row = []
    for j in Y:
        row.append((i,j))
    c0matrix.append(row)
print('\nPosition Matrix at t=0 sec is,\n')
for row in c0matrix:
    print(row)

# Step size (assumed equal to 0.1)
h = 0.1
# Component forces on each particle
def cforce():
    return np.random.uniform(-1,1)
# Velocity of a particle at t = 0 sec
def cvelocity():
    return np.random.uniform(-10,10)

# particle position matrix at t=1 sec
c1matrix = []
for i in range(len(c0matrix)):
    row = []
    for j in range(len(c0matrix)):
        xnew = c0matrix[i][j][0] + (h*cvelocity()) + ((h**2)*cforce()/2)
        ynew = c0matrix[i][j][1] + (h*cvelocity()) + ((h**2)*cforce()/2)
        # Rounding foating values upto 4 decimals
        xnew = round(xnew, 4)
        ynew = round(ynew, 4)
        row.append((xnew,ynew))
    c1matrix.append(row)

# print('\nPosition Matrix at t=1 sec is,\n')
# for row in c1matrix:
#     print(row)

# final position and velocity matrices after time t
time = int(input('\nMention the time iterval t: '))
if time == 0 or time == 1:
    print('\nPlease give correct time input.')

else:
    for t in range(time):
        cnmatrix = []    # Final position matrix after t sec
        for i in range(len(c1matrix)):
            row = []
            for j in range(len(c1matrix)):
                xfinal = (t * c1matrix[i][j][0]) - ((t-1) * c0matrix[i][j][0]) + ((h**2) * cforce())
                yfinal = (t * c1matrix[i][j][1]) - ((t-1) * c0matrix[i][j][1]) + ((h**2) * cforce())
                # rounding off upto 4 decimal
                xfinal = round(xfinal, 4)
                yfinal = round(yfinal, 4)
                row.append((xfinal,yfinal)) 
            cnmatrix.append((row))

# print('\nPosition Matrix at t sec is,')
# for row in cnmatrix:
#   print(row)

# Velocity matrix after t sec
vresultant = []  # resultant of vxfinal and vyfinal for each time instant
for t in range(2,time+1):
    vnmatrix = []
    for i in range(len(c1matrix)):
        row = []
        for j in range(len(c1matrix)):
            vxfinal = ((c1matrix[i][j][0] - c0matrix[i][j][0])/h)
            vyfinal = ((c1matrix[i][j][1] - c0matrix[i][j][1])/h)
            # rounding off upto 4 decimal
            vxfinal = round(vxfinal, 4)
            vyfinal = round(vyfinal, 4)
            row.append((vxfinal, vyfinal))
        vnmatrix.append(row)
    resultant_velocity = round(math.sqrt(vxfinal**2 + vyfinal**2),4)
    vresultant.append(resultant_velocity) 

# Temperature determination for each time instant
for t in range(2,time+1):
    continue

# Let's plot the position and velocity graphs.