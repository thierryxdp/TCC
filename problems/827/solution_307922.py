def qtd_divisores(numero):
    '''Função que conta quantos divisores um número possui;
    int -> int'''
    divisores=0
    lista = list(range(1,n+1))
    for elemento in lista:
        if n%elemento==0:
            divisores=divisores+1
    return divisores