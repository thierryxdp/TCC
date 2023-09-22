def qtd_divisores(numero):
    '''dado um número inteiro retorna a quantidade
    de divisores que este número possui.'''
    qtd=0
    for n in range(1,numero+1):
        if numero%n==0:
            qtd=qtd+1
    return qtd