def soma_h(n):
    '''retorna o valor de h com n termos'''
    lista = []

    for i in range(1, n+1):
        lista.append(1/i)

    return round (sum(lista),2)