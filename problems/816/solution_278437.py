def maiores (inteiros, numero_n):
    lista= inteiros+[numero_n]
    list.sort(lista)
    del lista[0:numero_n+1]
    return lista