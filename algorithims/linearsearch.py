arr = [2,5,9,6,3,1,7,8]
t = 9

def linearseacrch(target, array):
    for i in range(len(array)):
        if target == array[i]:
            return i
        

print(linearseacrch(t,arr))

#time complexity = O(n)