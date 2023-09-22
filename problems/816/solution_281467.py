def maiores(lista,n):
        n=int
        lista=list.sort(lista)
        del lista[0:n]
        return lista