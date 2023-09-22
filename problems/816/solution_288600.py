def maiores(lista,n):
    """Esta funcao recebe uma lista e um numero e avalia quais numeros da lista são maiores que o numero fornecido
    list -> list"""
    l = []
    for x in range(len(lista)):
        if lista[x] > n:
            l.append(lista[x])
    l.sort()
    return l