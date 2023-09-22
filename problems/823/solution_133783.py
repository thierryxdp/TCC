def faltante(lista):
    """retorna a peça faltante dada uma lista
    list-> int"""
    if 1 not in lista:
        return 1
    lista = list.sort(lista)
    proximo = 1
    anterior = 0
    resposta = 0
    while proximo < list.range(lista):
        if lista[anterior] != lista[proximo] - 1:
            return lista[proximo] - 1
        proximo += 1