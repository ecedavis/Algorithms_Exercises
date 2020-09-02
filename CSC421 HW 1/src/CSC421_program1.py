

def elementMatch(x,y):
    count = 0
    i=0
    j=0
    n=len(x)
    
    while(i<n and j<n):
        count+=1
        if x[i]==y[j]:
            return True
        if x[j]<y[i]:
            j+=1
        else:
            i+=1
    return False

nuts =[5,10,20,30,35,60,110,2100]
bolts = [15,110,120,130,135,160,1110,2100]

print(elementMatch(nuts,bolts))
print()









def equalssum(x, total):
    count = 0
    i=0
    n=len(x)
    j=n-1
    count=0
    
    while(i<j):
        count+=1
        diff = total-x[i]
        if x[j]==diff and x[i]!=x[j]:
            return True
        elif x[j]>diff:
            j-=1
        else:
            i+=1
    return False

nums = [5,10,20,30,35,60,110,200]

for test in nums:
    print(equalssum(nums,test))




def equalssum3(x, total):
    count = 0
    i=0
    n=len(x)
    c1=0
    c2=0
    for num in x:
        c1+=1
        diff = total - num
        i=0
        j=n-1
        while(i<j):
            c2+=1
            sum=x[i]+x[j]
            if sum==diff and x[i]!=x[j] and x[j]!=num and x[i]!=num:
                return True
            elif sum>diff:
                j-=1
            else:
                i+=1
    
    return False

nums = [5,10,20,30,35,60,110,200]

for test in nums:
    print(equalssum3(nums,test))
    
        


    
    
    
    #print(x[i]," ", x[j], " ", x[k], " - curSum=",curSum, " total=", total)
                