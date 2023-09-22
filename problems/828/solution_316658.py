def primo(num):
    '''função que verifica se o número de entrada é primo ou não.
    num -> int
    return -> bool'''
    num_primo = 0
    
    for divisores in range(2, num + 1):
        if num % divisores == 0:
            num_primo += 1
            
        if num_primo == 1
            return True