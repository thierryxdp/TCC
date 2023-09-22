def maiores (inteiros, numero_n):
    lista= inteiros+[numero_n]
    list.sort(lista)
    num= list.index (lista,numero_n)
    del lista[0:num+1]
    return lista