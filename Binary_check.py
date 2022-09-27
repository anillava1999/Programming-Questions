# Python program to check number representation is in binary

input_value = 10111
while (input_value > 0):
    last_digit = input_value % 10
    if(last_digit != 0 and last_digit != 1):
        print("it's  not binary")
        break
    input_value = input_value // 10
    
if(input_value == 0):
    print("It's binary")
    
        
    
