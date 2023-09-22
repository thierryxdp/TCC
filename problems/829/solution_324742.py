def soma_h(n):
    soma = 0
    '''
    for x in range(1, n + 1):
        soma = soma + (1 / x)
    '''
    contador = 0
    lista = range(1, n + 1)
    while contador < len(lista):
        x = lista[contador]
        soma = soma + (1 / x)
        contador = contador + 1
    return round(soma, 2)