arr = [1,2,5,9,50,3,6,8,4,0]

def ss(array, sp):
    for i in range(sp, len(array)):
        mi = i

        for j in range(i+1, len(array)):
            if array[j] < array[mi]:
                mi = j

        array[i],array[mi] = array[mi],array[i]


    return array


print(ss(arr,0))