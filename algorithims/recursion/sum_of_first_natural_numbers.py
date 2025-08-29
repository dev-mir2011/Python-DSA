def sofnn(num):
    if num == 0:
        return 0
    
    else:
        return num + sofnn(num -1)

print(sofnn(5))