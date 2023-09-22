def maiores(lista,n):
        lista.append(n)
        sorted(lista)
        x = lista.index(n)
        return lista[x:]