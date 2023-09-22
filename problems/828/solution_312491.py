def primo(n):
    '''
    Recebe um número n (inteiro) e checa se ele é primo, retornando
    um booleano
    '''
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True