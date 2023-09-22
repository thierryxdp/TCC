def primo(x:int)->bool:
    '''Dado um número inteiro positivo, 
    é indicado se ele é ou não primo.'''
    num_primo = True
    divisor = 2
    
    while divisor < x and num_primo:
        if x % divisor == 0:
            num_primo = False
        divisor += 1
          
    if num_primo and n != 1: 
        return True
    else:
        return False