def rotation(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):

    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def array(a,a_size):

    for i in range(a_size):
        print(a[i], end = " ")
    print("\n")

a = [1,2,5,9,6,3,7,8]
array(a,len(a))
rotation(a,2,len(a))
array(a,len(a))