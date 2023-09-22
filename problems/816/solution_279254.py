def maiores(lista,n):
        y = lista
        for i in range(len(lista)):
                if lista[i]<n:
                    del y[i]  
                    k=y.sort()
                    return k
                else:
                    return lista.sort()