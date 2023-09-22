def faltante(lista):
    list.reverse(lista)
    num=lista[0]
    list.sort(lista)
    i=0
    while i<num:
        if i!=lista[i]:
            return i