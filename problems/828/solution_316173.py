def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''
    divisores=[]
    i=0
    for i in range(2,n):
        if n%i==0:
            i=i+1          
    return i