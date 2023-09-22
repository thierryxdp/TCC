def maiores(lista,n):
    lista.sort(reverse = False)
    i = 0
    while i < n:
        listanova = lista.remove(i)
        return lista