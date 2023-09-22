def primo(n):
    '''Retorna se um número inteiro positivo é primo ou não;
    int -> bool'''
    multiplos = 0
    for i in range(2,n):
        if n%i == 0:
            multiplos += 1    
    if multiplos == 0:
        return True
    else:
        return False