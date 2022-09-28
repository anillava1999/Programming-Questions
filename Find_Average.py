## Python code to find the average of numbers

A = [12,30,40,50]
size = len(A)
B = 0
for i in range(0,size):
    B = B + A[i]
    print(B)
avg=B/size
print(avg)
