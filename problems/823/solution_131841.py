def faltante(lista):
    for i in lista:
        if lista[i+1] ==  i+1:
            i=i+1
            return i+1