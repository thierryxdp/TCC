def soma_h(n):
    '''Calcula o somatorio de uma lista que contém todos os valores inversos de 1 a n
    int -> float'''
    lista = []
    for x in range(1, n+1):
        valor = 1/x
        lista.append(valor)
    return round(sum(lista), 2)