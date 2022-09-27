## Python program for palindrome number using iterative method

## we are using reverse technique to find palidrome number

input_Value = 121
duplicate = input_Value
reverse_digit = 0
while ( input_Value > 0):
    lastdigit = input_Value % 10
    reverse_digit = (reverse_digit * 10) + lastdigit
    input_Value = input_Value // 10

    
if (reverse_digit == duplicate) :
    print("It's Palidrome")
else :
    print("It's not Palidrome")
