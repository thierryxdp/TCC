def primo(n):
    ''' Função que,dado um número inteiro positivo, verifica se este é primo ou não,
    retornando um valor booleano.
    int-->bool'''
    contador = 0
    for i in range(2,n):
        if (n % i == 0):  
            contador = contador + 1
    if contador == 0:
        return True
    else :
        return False