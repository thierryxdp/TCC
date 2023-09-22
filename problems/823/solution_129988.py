def faltante(lista):
    list.reverse(lista)
    list.sort(lista)
    i=1
    while i<list.index(lista,lista[i]):
        return i
    i+=1