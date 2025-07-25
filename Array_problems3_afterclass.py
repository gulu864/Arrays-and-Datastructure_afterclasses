def func(a,a_size):
    
    zero = []
    one = []
    two = []

    for i in range(1,a_size):

        if 0 == a[i]:
            zero.append(0)

        elif 1 == a[i]:
            one.append(1)
        
        elif 2 == a[i]:
            two.append(2)
    

    print("Sorted zero,ones and twos in array: ",zero,one,two)


a = [1,2,0,2,1,0,1,1,1,0,2,2,0,1,2,2]
a_size = len(a)
print(a)
print(func(a,a_size))