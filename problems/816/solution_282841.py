def maiores(lista,n):
    ordenada=list.sort(lista,reverse=True)
    posicao=list.index(ordenada,n)
    maiores=ordenada[0,posicao]
    if n in ordenada:
        return list.reverse(maiores)