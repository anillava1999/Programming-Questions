# Python program to print Fibonacci series program in using Iterative methods

input_value =  5
back_first = 1
back_second = 0
temp = 0
for i in range(input_value):
        print(back_second)                  # accessing fibonacci series using swap case technique
        temp = back_second + back_first    
        back_second = back_first 
        back_first = temp                  


