import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('./populations.txt')
year, hares, lynxes, carrots = data.T # trick: columns to variables
datarr = np.array([year,hares,lynxes,carrots])
print(datarr)
sort = np.argsort(datarr,axis=1)

print("The mean of hares is:")
print(np.mean(hares))
print("The std of hares is:")
print(np.std(hares))
print("The mean of lynxes is:")
print(np.mean(lynxes))
print("The std of lynxes is:")
print(np.std(lynxes))
print("The mean of carrots is:")
print(np.mean(carrots))
print("The std of carrots is:")
print(np.std(carrots))

print("The max num of hares is:")
print(np.amax(hares))
print(datarr[0:2,3])
indices = sort[1:2,-1:]
mh = np.take(datarr,indices)
print(mh)

print("The max num of lynxes is:")
print(np.amax(lynxes))
print(datarr[0::2,4])
indices = sort[2:3,-1:]
ml = np.take(datarr,indices)
print(ml)

print("The max num of carrots is:")
print(np.amax(carrots))
print(datarr[0::3,0])
indices = sort[3:,-1:]
mc = np.take(datarr,indices)
print(mc)

print("Population data only")
datarr2 = np.array([hares,lynxes,carrots])
print(np.argsort(datarr2,axis=0))

print("Is the popluation greater than 50000?")
gt = datarr2.__gt__(50000)
print(np.any(gt))
print(np.any(gt,axis=0))

print("The top 2 years with the lowest population")
ty = np.argsort(datarr,axis=1)
indices = ty[1:,0:2]
#print(indices)
tty = np.take(datarr,indices)
print(tty)

#print(help(np.gradient))
ghares = np.gradient(hares)
print("The correlation coefficient between hares and lynxes is:")
print(np.corrcoef(ghares,lynxes))
print("The correlation coefficient for hares is:")
print(np.corrcoef(ghares))

plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, ghares, year, lynxes)
plt.legend(('Hare', 'Lynx'), loc=(1.05, 0.5))
plt.ylabel('population')
plt.xlabel('years')
plt.title('Change in Hares vs Lynx Population')
plt.show()
