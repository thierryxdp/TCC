def faltante(lista):
    '''informa qual peça está faltando de um quebra cabeça de lista N - 1
    list -> int'''
    tamLista = len(lista) + 1
    n = 1
    pecas = [n]
    while n < tamLista:
        pecas += [(n+1),]
        n = n+1
    total_esperado = sum(pecas)
    total_observado = sum(lista)
    return total_esperado - total_observado