#sets and dictionaries
a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])
print a.union(b)

band = ['mel', 'geri', 'victoria', 'mel', 'emma']
counts = {}
for member in band:
    if member not in counts:
        counts[member] = 1
    else:
        counts[member] += 1
for member in counts:
    print member, counts[member]

if {}:
    print 'gg','hello', 'hh'

d = {'maggie':'uk', 'ronnie':'usa'}
print d
print dir(d)
print 'These are the items in d', d.items()
print 'These are the keys in d', d.keys() 
print 'These are the values in d', d.values()
print d.get('maggie','nowhere')
print d.setdefault('kwesi','ghana')
print d

#numpy's they function as a list of same class, hence faster!

import numpy as np
x = range(1,11)
a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)
print a1.dtype
print a2.dtype


ze = np.zeros((2,3,4))
on = np.ones((2,3,4))
print ze, on
arr = np.arange(1000)
#print arr

#slicing with numpy
a = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
print a[1]
print a[1:4]

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],[1, 22, 4, 0.1, 5.3, -9],[3, 1, 2.1, 21, 1.1, -2]])

print 'This is:', a
print 'h', a[:, 3], 'h' #prints every fourth item in array
print 'j', a[1:4, 0:4], 'j' #
print 'p', a[1:, 2], 'p'

arr = np.array([range(4),range(10,14)])
print np.shape(arr)
print np.size(arr)
print np.max(arr)
print np.min(arr)


print np.reshape(arr, (2,2,2))
print np.transpose(arr)
print np.ravel(arr)
print arr.astype(np.float32)

print 'Starting a new exercise'

a = np.array([range(4),range(10,14)])
print a
b = np.array([2, -1, 1, 0])
print a * b
b1 = b * 100
b2 = b * 100.0
print b1, b2
print b1 == b2
print type(b1)
print type(b2)

arr = np.array(range(0,10))
#print arr < 3
print np.less(arr,3)

condition = np.logical_or(arr < 3,arr > 8) #arr less than 3 or greater than 8
new = np.where(condition, arr *5, arr *-5)
print new

def solMag(u,v, minmag = 0.1):
    mag = (u**2 + v**2)**0.5
    output = np.where(mag > minmag, mag, minmag)
    return output
u = np.array([[4,5,6],[2,3,4]])
v = np.array([[2,2,2],[1,1,1]])
print solMag(u,v)


#masking in numpy
import numpy.ma as MA

marr = MA.masked_array(range(0,10), fill_value = -999)
marr[2] = MA.masked
print marr
print marr.mask
narr = MA.masked_where(marr > 6,marr) #apply a mask when value is greater than 7 to leave those less than 7
print narr
print narr.fill_value

x = MA.filled(narr)
print x


m1 = MA.masked_array(range(1,9))
print m1
m2 = m1.reshape(2,4)
print m2
m3 = MA.masked_greater(m2, 6)
print m3*100

differ = m3 - np.ones((2, 4))
print differ
print type(differ)

#matplotlib
times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [0,0.5,1,1.2], 'g--', label = "Some data")
plt.plot(times, [1, 2, 3, 4], 'r', label = "Other data")
plt.title('Concentration of Chlorine vs Time')
plt.ylabel('Concentration (%)')
plt.xlabel('Time (s)')
plt.legend()
plt.savefig('kwesi.png')
#plt.show()

Temp = [14.1,15.5,16.3,18.1,17.3,19.1,20.2]
Time = [0, 1, 2, 3, 4, 5, 6]
CO2  = [250, 265, 272, 260, 300, 320, 389]
fig, ax1 = plt.subplots()
ax1.plot(Time,CO2, 'g--')
ax1.set_ylabel('CO2', color = 'g')
ax2 = ax1.twinx()
ax2.plot(Time,Temp, 'r')
ax2.set_ylabel('Temp',  color='r')
plt.show()



