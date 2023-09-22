def maiores(lista: list, n: int):
    """comentário"""
    i = 0
    lista_maiores = []
    if lista[i] > n:
        lista_maiores += [lista[i],]
        i =+ 1
        return lista_maiores
    else:
        return lista_maiores