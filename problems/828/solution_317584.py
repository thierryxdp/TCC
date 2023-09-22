def primo(n):
    ''' 
    Funçao que dado um numero positivo, verifica se ele é´primo ou nao e retorna
    um valor booleano.
    int -> bool
    '''
    divisores = 0
    for i in range(2,n+1):
        if n%i == 0:
            divisores = divisores + 1
            if divisores != 2:
                return False
            elif divisores == 2:
                return True