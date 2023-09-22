def faltante(lista):
    i=1
    while i<len(lista):
        if list.count(lista,i)==0:
            return lista[1]
        else:
            i=i+1