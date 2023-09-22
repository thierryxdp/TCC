def primo(num):
    '''função que verifica se o número de entrada é primo ou não.
    num -> int
    return -> bool'''
    num_primo = 0
    
    for divisores in range(2, num):
        if num % divisores == 0:
            num_primo += divisores
            
        if num_primo = num:
            return True