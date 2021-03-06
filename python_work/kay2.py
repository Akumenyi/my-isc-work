name = "Kwesi"

#recap working with the "if, elif and else"
if name == "Temi":
    print "Hi Temi"
elif name == "Kwesi":
    print "Hello"
else:
    print "Who are you?" 


#excercise on tuples
t = (1,)
print t[0]
x = range(100, 201)
print x
tom = tuple(x)
print tom[0], tom[-1]


#using enumerate
mylist = [23, "hi", 2.4e-10]
for (count,item) in enumerate(mylist):
    print count,item 


#unpack list to tuple in a line
(first,middle,last) = mylist
print "values are", first, middle, last
first,middle,last = middle,last,first
print first, middle, last
print 'Done!'


#read write manipulate data
with open('weather.csv', 'r') as reader:
    data = reader.read()
print data


with open('weather.csv', 'r') as reader:
    line = reader.readline()
    while line:
        line = reader.readline()
        print line
    print "It's over"

with open('weather.csv', 'r') as reader:
    rf = reader.readline()		#read headers
    print 'rf reads headers:', rf
    rain = []
    for line in reader.readlines():
        r =float(line.strip().split(",")[-1])
        rain.append(r)
print rain
with open('myrainfall.txt','w') as writer: #write rain output to text str
    for r in rain:
        writer.write(str(r) + '\n')

#advanced data manipulation
import struct 
bin_data = struct.pack("bbbb", 123, 12, 45, 34) #pack into 4 bytes
with open('mybinary.dat', 'wb') as bwriter:     #using with, wrt to file
    bwriter.write(bin_data)                     #called bin_data
with open('mybinary.dat', 'rb') as breader:
    bin_data2 = breader.read()
data = struct.unpack("bbbb", bin_data2)		#unpack into bin_data2
print 'Data is:', data				#print data


#dealing with strings
s = "I love to write python"
for a in s:
    print a
b = s[4]
print b
c = s[-1]
print c
print 'length is ',len(s)
print s[0], s[0][0], s[0][0][0]

s = "I love to write python"
split_s = s.split()
for word in split_s:
    if word.find("i") > -1:
        print "I found 'i' in: '{0}'".format(word)    

something = "Completely Different"
print 'printing directory...',dir(something)
print something.count('t')
print something.find('plete')
print something.split('e')
thing2 = something.replace('Different','Silly')
print thing2
#something[0] = 'B' #gives error cos strings are immuatable!!

#using aliases
a = [0, 1, 2]
b = a
print a, b
b[0] = "hello"
print a, b
a.append(3)
print a, b

a = "can I change"
b = a
print a, b
b = 'different'
print a, b

import copy
a = [0, 1, 2]
b = copy.deepcopy(a)
print a, b
b[0] = 'hello'
print a, b


#functions
def double_it(number):
    return 2 * number
print 'The answer is',double_it(2)
print 'The answer is',double_it('hello')
print 'The answer is',double_it(3.145673)

def calc_hypo(a,b): #function to calculate hypotenuse of a triangle
    hypo = (a**2 + b**2)**0.5
    return hypo
print 'The hypotenuse is',calc_hypo(3,4)


def calc_hypo(a,b): #add checks into function code
    if type(a) not in (int,float) or type(b) not in (int,float):
        print 'a bad argument'
        return False
    if a <= 0 or b <=0:
        print 'a bad argument'
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo 
print 'The hypotenuse is',calc_hypo('hi','alright')


pi = 3.145   #calc the area of a circle
def area(r):
    area = pi * r**2
    return area
print 'The area of the circle is',area(3)

def volume(r):   #calc the volume of a sphere
    volume = 1.333 * pi * r**3
    return volume
print 'The volume of the sphere is',volume(3)


#using scripts and libraries
"""mkdir dancing
cd dancing/
gedit _init_.py
cd ../
python -c "import dancing"
"""

#sets and dictionaries
a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])
print a.union(b)
