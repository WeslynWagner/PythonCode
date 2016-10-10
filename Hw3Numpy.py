#!/usr/bin/env Python

import numpy as np
import matplotlib.pyplot as plt

matrix = np.arange(6)+np.arange(0,51,10)[:,np.newaxis]
print("1. This is the matrix\n" + str(matrix))


two = matrix[:,2]
print("this is the array containing items in RED " + str(two))

three = matrix[0,3:5]
print("this is the array containing items in ORANGE " + str(three))

four = matrix[2:5:2,::2]
print("this is the array containing items in GREEN " + str(four))

five = matrix[4:,4:]
print("this is the array containing items in BLUE " + str(five))
print("")
print("Creating some arrays")
t = np.ones((4,4),dtype='int32')
t[2][3] = 2
t[3][1] = 6
print(t)
print("")
w = np.diag(np.array([2,3,4,5,6],dtype='float'))
w = np.insert(w,0,[0.,0.,0.,0.,0.],axis=0)
print(w)

fig1 = plt.figure(1)
t = np.arange(-np.pi, np.pi, 0.1)
s = np.cos(t)
plt.plot(t,s)
plt.ylabel("units")
plt.xlabel("units")
plt.title("Cosine in Python")


fig2 = plt.figure(2)
t = np.arange(-np.pi, np.pi, 0.1)
s = np.sin(t)
plt.plot(t,s,label='Sin')
plt.ylabel("units")
plt.xlabel("units")
plt.title("Sine in Python")


fig3 = plt.figure(3)
t = np.arange(-np.pi, np.pi, 0.1)
s1 = np.cos(t)
s2 = np.sin(t)
fig3,ax3 = plt.subplots()
ax3.plot(t,s1,label='Cos')
ax3.plot(t,s2,label='Sin')
legend3 = ax3.legend(loc='upper right')
ax3.set_ylabel("units")
ax3.set_xlabel("units")
ax3.set_title("Both in Python")


fig4 = plt.figure(4)
t = np.arange(-np.pi, np.pi, 0.1)
s1 = np.cos(t)
s2 = np.sin(t)
f,axarr = plt.subplots(2,sharex=True)

axarr[0].plot(t,s1,label='Cos')
axarr[0].set_ylabel("units")
axarr[0].set_title("Cosine in Python")
legend1 = axarr[0].legend(loc='upper right')

axarr[1].plot(t,s2,label='Sin')
axarr[1].set_ylabel("units")
axarr[1].set_xlabel("units")
axarr[1].set_title("Sine in Python")
legend2 = axarr[1].legend(loc='upper left')
plt.show()
