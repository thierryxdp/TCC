def maiores(lista,n):
        lista=list.sort(lista)
        a=lista.index(n)
        del lista[0:a]
        return lista