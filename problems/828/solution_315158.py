def primo(n):
    '''Funcao que, dado um numero inteiro positivo, diz se ele é primo ou nao'''
    '''int -> bool'''
    
    for x in range(2,n):
        if n % x ==0:
            return False
    else:
            return True