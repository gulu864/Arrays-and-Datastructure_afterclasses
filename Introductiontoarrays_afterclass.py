def reverse(a,a_size,n):

    temp = 0

    while(temp<a_size):

        start = temp
        end = min(temp + n - 1,a_size - 1)

        while (start < end):

            a[start], a[end] = a[end], a[start]
            start +=1
            end -= 1

        temp+= n
    return a

a = [1,23,2,31,2,4,73,41,3,64]

arr_size = len(a)
n = arr_size
b = reverse(a,arr_size,n)

for i in range(0,arr_size):
    print(b[i],end=" ")