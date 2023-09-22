def maiores(lista: list, n: int):
    """comentário"""
    i = 0
    lista_maiores = []
    while i > len(lista):
        if lista[i] > n:
            lista_maiores = lista_maiores + [lista[i],]
        i = i+ 1
    
    return lista_maiores