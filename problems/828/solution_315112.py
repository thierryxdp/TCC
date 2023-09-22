def primo(numero):
    '''retorna se um numero é primo ou nao'''
    '''int -> bool'''
    
    divisor = 1
    
    while divisor <= numero:
        if numero%divisor==0:
    return False