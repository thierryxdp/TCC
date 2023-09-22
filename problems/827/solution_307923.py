def qtd_divisores(numero):
    '''Função que conta quantos divisores um número possui;
    int -> int'''
    divisores=0
    lista = list(range(1,numero+1))
    for elemento in lista:
        if numero%elemento==0:
            divisores=divisores+1
    return divisores