def qtd_divisores(numero):
    '''funcao que conta quantos divisores um número tem;
       int=>int'''
    contador = 0
    for i in range(1, numero):
        if numero % i == 0:
            contador = contador+1
    if numero<0:
        return contador
    else:
        return contador+1