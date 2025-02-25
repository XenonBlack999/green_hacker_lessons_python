# binary to decimal changer function 

def binary_to_decimal(b):
    num = b
    dec = 0
    base = 1 # because 2^0=1
    temp = num
    while(temp): 
        digit = temp%10 
        temp = int(temp/10)
        dec += digit * base
        base = base * 2
    return dec
        
bnum = 101010

print(binary_to_decimal(bnum))
