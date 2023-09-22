def qtd_divisores(numero):
    '''Função que calcula quantos divisores um número possui; int -> int'''
    soma=0
    for n in range(1,numero+1):
        if numero%n==0:
            soma=soma+1
    return soma