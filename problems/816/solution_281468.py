def maiores(lista,n):
        lista=list.sort(lista)
        del lista[0:n]
        return lista