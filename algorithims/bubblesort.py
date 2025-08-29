arr = [2,5,9,6,3,1,7,8]

def sort(array) -> list:
    for i in range(len(array)):
        left = 0
        right = 1

        while right < len(array):
            if array[left] > array[right]:
                array[left], array[right] = array[right], array[left]

            
            right += 1
            left += 1


    return array
    
print(arr)
print(sort(arr))

#time complexity = O(n^2)