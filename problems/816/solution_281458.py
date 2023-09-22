def maiores(lista,n):
        list.sort(lista)
        a=list.index(n)
        del lista[0:a]
        return lista