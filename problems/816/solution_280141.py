def maiores(lista,n):
    lista1 = lista.sorted()
    if n in lista1:
        posicao = lista.index(n)
        return posicao