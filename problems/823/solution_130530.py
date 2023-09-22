def faltante(lista):
    cont = 0
    while cont < len(lista):
        if lista[cont]-lista[cont-1] > 1:
            lista.sort()
            return lista[cont-1]+1
        if 1 not in lista:
            return 1
        if len(lista)+1 not in lista:
            return len(lista)+1
       
        cont = cont +1
    return lista