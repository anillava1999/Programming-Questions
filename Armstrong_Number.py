Number = 154
Duplicate = Number                        # Making duplicate input
Add_Ele = 0
while(Number > 0 ) :
    LastDigit = Number % 10               # Finding last digit in number
    K = LastDigit ** 3                    # Calculating the single digit with cube
    Add_Ele = Add_Ele  + K                # Adding each digits cube value to third variable
    Number = Number // 10                 # Removing last digit in number
    
if (Duplicate == Add_Ele):
    print("This is Armstrong Number")
else :
    print("Sorry this is not Armstrong Number")
