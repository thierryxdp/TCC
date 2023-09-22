def primo(num):
    """ Dado um numero verifica se o número é primo..
    entrada intero -> booleando"""
    
    d = list(range(3,num,2))
    
    for proximo in d:
        if num%proximo == 0:
            return bool 
    return bool