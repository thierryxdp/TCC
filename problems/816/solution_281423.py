def maiores(lista,n):
        list.sort(lista)
        x=list.index(n)
        del lista[0:x]
        return lista