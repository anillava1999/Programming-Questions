# Python program to check given number is prime or not

Input = 9
if(Input > 1) :                                     # Finding input is greater 1 or not 
    result = Input % 2                              # Findind remainder for the input
    if(result == 1) :                               # if the remaider is 1 it's prime, if remainder is 0 it's not prime
        print(" This number is Prime")
    else :
        print(" Sorry this is not prime number")
    
