def maiores(lista,n):
        list.sort(lista)
        del lista[0:n+3]
        return lista