## program to check a given number is perfect or not in Python


num = int(input("please give first number a: "))
sum=0
for i in range(1,(num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i   
if sum == num:
    print("given no. is perfect number")
else:
    print("given no. is not a perfect number")
