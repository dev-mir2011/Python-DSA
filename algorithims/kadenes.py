arr = [-2,3,2,-1]

def k(a):
    mc = mg = a[0]
    for i in range(1,len(a)-1):
        mc = max(a[i],mc+a[i])

        if mc > mg :
            mg = mc

    
    return mg


print(k(arr))