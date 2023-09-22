def maiores(lista,n):
    ordenada=list.sort(lista,reverse=True)
    maiores=ordenada[0,list.index(ordenada,n)]
    if n in ordenada:
        return list.reverse(maiores)