def primo(n):
    '''dado um número n qualquer, retorna se é primo ou não
    int --> bool'''
    
    divisores = 0
    for numero in range(1,int((n**0.5)+1)):
        if n % numero == 1:
            divisores += 1
            
    return divisores < 2