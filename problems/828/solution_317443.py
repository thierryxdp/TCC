def primo(n):
    '''Retorna se um número é ou não primo
    int --> bool'''
    divisores = 0
    for numero in range(0,int((n**0.5)+1)):
        if n % numero == 0:
            divisores += 1
            
    return divisores < 2