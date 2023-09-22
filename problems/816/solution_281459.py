def maiores(lista,n):
        lista=list.sort(lista)
        a=list.index(lista,n)
        del lista[0:a]
        return lista