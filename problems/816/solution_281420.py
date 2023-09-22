def maiores(lista,n):
        list.sort(lista)
        del lista[0:n]
        return lista