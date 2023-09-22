def soma_H(n):
    '''retorna a soma H com n inteiros, onde n é inteiro, retorn com duas casas decimais
    int->float'''
    soma=0
    for i in range(1,n+1):
        n=1/i
        soma+=n
    return round(soma,2)