'''
Mark Davis
CSC 412
Assignment 1
Due October 5, 2018
'''
import math

def angle2pi (y,x):
    if y<0:
        return math.atan2(y,x) + (2*3.1415)
    return math.atan2(y,x)


filename = "case6.txt"
file=open(filename, "r")

pairs = []
coordinates = file.readlines()

minx = 1111111111
miny = 1111111111
for line in coordinates:
    pairs.append(line.split())

minypairs = []
for pair in pairs:
    pair[0]=int(pair[0])
    pair[1]=int(pair[1])
    if pair[1] <= miny:
        miny=pair[1]

for pair in pairs:
    if pair[1]<=miny:
        minypairs.append(pair)

p0 = []
for pair in minypairs:
    if pair[1]==miny and pair[0]<minx:
        minx=pair[0]
        p0=pair


#print ("p0 =",p0)
#print ("initial pairs = ",pairs)
pairs.remove([p0[0],p0[1]])
#print ("remaining pairs = ",pairs)

#calculate polar angle
for i in range(len(pairs)):
    pair = pairs[i]
    angle=round(angle2pi((pair[1]-p0[1]),(pair[0]-p0[0])),2)
    pair.append(angle)


#print("with angles = ",pairs)

sortedPairs = sorted(pairs,key=lambda x: x[1])
sortedPairs = sorted(pairs,key=lambda x: x[2])
#print("sorted by angle = ",sortedPairs)
p0.append(sortedPairs[0][2])


minPair = p0
i=0
while i < len(sortedPairs)-1:
    at = sortedPairs[i]
    if at[2] > minPair[2]:
        minPair = at
        i+=1
        continue
    if (at[2] == minPair[2]) and (sortedPairs[i+1][2]==minPair[2]):
        sortedPairs.remove(at)
        continue
    i+=1
#print("filtered pairs = ",sortedPairs)

tempStack = []
if len(sortedPairs)<3:
    tempStack.append(p0)
    for pair in sortedPairs:
        tempStack.append(pair)
    #print(tempStack)
else:
    tempStack.append(p0)
    tempStack.append(sortedPairs[0])
    tempStack.append(sortedPairs[1])
    #print ("tempStack",tempStack)
    pointA = sortedPairs[0]
    pointB = sortedPairs[1]
    i=2
    while i < len(sortedPairs):
        #a = point i-1
        #b == point i
        #if angle from a to be is positive, the right turn
        # pop point a if a->b is right turn
        pointC = sortedPairs[i]
        #print(pointC)
        angleAB = angle2pi((pointB[1]-pointA[1]),(pointB[0]-pointA[0]))
        angleAC = angle2pi((pointC[1]-pointA[1]),(pointC[0]-pointA[0]))
        #print ("angleAB = ",angleAB)

        #print("\ntempStack = ", tempStack)
        if (angleAC-angleAB <=0):
            tempStack.pop()
            pointB=tempStack[-1]
            pointA=tempStack[-2]
            #print("tempStack = ", tempStack)


        else:
            pointA=pointB
            pointB=pointC
            tempStack.append(pointC)
            i+=1
        #print("tempStack = ", tempStack)


for pair in tempStack:
    print("{:d}, {:d}".format(pair[0],pair[1]))