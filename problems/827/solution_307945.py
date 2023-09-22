def qtd_divisores(numero):
    '''Dado um número inteiro retorna quantos divispres este número possui.
    int -> int'''
    qtd=0
    for n in range(1,numero+1):
        if numero%n==0:
            qtd=qtd+1
    return qtd