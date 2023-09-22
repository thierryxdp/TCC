def maiores (lista, n):
    if n not in lista:
        lista=lista.extend(n)
        lista_=sorted(lista)
    return lista_[:n]