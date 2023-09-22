def fatorial(n):
    '''dado um numero inteiro n, essa funcao calcula o fatorial desse numero
    int-->int'''
    resultado=n
    i=n
    while(i!=1):
        i-=1
        resultado*=i
    return resultado