def  filtraMultiplos(lista, n):
    """ função que retorna uma lista contendo os numeros divisiveis pro n
    lista, int -> lista"""
    divisiveis = []
    i = 0
    while i < len(lista):
        divisiveis = divisiveis + [i for i in lista if i % n == 0]
        i = i + 1
        break
    return divisiveis