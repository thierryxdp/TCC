def faltante(lista):
    list.sort(lista)
    i=1
    while i in lista:
        if i not in lista:
            return i
        else:
            i=i+1