def maiores(lista,n):
        lista.append(n)
        sorted(lista)
        x = lista.index(n)
        lista.remove(n)
        return lista[x:]