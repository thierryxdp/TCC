def maiores(lista,n):
        type(n)=int
        lista=list.sort(lista)
        del lista[0:n]
        return lista