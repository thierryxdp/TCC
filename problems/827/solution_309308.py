def qtd_divisores(numero):
    '''a funcao retorna o numero de divisores do numero de entrada
    int-> int'''
    divisores=0
    for i in range(1, numero+1):
        if numero%i == 0:
            divisores= i+1
    return divisores