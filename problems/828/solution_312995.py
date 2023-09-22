def primo(n):
    '''Dado um numero inteiro positivo (n), verifica se 
    este numero e primo ou nao.
    int->bool'''
    
    divisores=range(2,n)
    for divisor in divisores:
        if n%divisor==0:
            return False
        
    return True