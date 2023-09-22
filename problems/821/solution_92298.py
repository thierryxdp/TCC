def fact(num): 
    if num < 0: 
        return 'Factorial of negative num does not exist'

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact