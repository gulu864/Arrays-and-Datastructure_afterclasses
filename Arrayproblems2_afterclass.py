def diffrence(a,a_size):
    
    maximum = 0
    diff = 0

    for i in range(1,a_size):
        diff = a[i] - a[i-1]
        
        if maximum < diff:
            maximum = diff
    return maximum

a = [5,7,3,9]

value = diffrence(a,len(a))
print("Diffrence: ",value)