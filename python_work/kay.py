mylist = [23, 'hi', 2.4e-10]    #make a list
count = 0     #initiate a counter
while count < 3 :        #start a loop
    item = mylist[count]
    print item,mylist.index(item)    #print both item and its postion
    count +=1


x=1
if x: print x, "is True"
if 22.1: print "True"
if "hello": print "True"
if 0: print "True"
if 0.0: print "True"


mylist2 = [1, 2, 3, 4, 5]
print mylist2[1]
print mylist2[1:5]
print mylist2[:]
print mylist2[1:4]

one_to_ten = range(1, 11)
one_to_ten[0] = 10
one_to_ten.append(11)
print one_to_ten
one_to_ten.extend([12, 13, 14])
print one_to_ten
backward = []
forward = []

values = ["a", "b", "c"]
for value in values:
   print value
   forward.append(value)
   backward.insert(0,value) #at first index put the value
print "Forward is:", forward
print "Backward is:", forward[::-1]



