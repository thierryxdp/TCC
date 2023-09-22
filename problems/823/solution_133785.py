def faltante(lista):
    """retorna a peça faltante dada uma lista
    list-> int"""
    if 1 not in lista:
        return 1
    list.sort(lista)
    proximo = 1
    anterior = 0
    resposta = 0
    while proximo < len(lista):
        if lista[anterior] != lista[proximo] - 1:
            return lista[proximo] - 1
        proximo += 1
        anterior += 1
    else:
        return lista[-1] + 1