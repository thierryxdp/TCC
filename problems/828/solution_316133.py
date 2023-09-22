def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''
    i=0
    for i in range(1,x+1):
        if n%i==0:
            i=i+1
    return i