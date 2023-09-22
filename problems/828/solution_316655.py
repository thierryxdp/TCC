def primo(num):
    '''função que verifica se o número de entrada é primo ou não.
    num -> int
    return -> bool'''
    
    
    for divisores in range(2, num):
        if num % divisores != 0:
            return True