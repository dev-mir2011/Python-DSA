arr = [1,2,5,9,50,3,6,8,4,0]
t = 10
def bs(target,array,) -> bool:
    array = sorted(array)
    left = 0
    right = len(array)-1

    while left<=right:
     
     mid = (left+right)//2

     if array[mid] == target:
        return True
    

     elif target < array[mid]:
        right = mid-1
        #return bs(target,array,left,mid-1)
    
     else:
        left = mid+1
        #return bs(target, array, mid+1, right)


    return False


print(bs(t,arr))

#time complexity = O(log(n))