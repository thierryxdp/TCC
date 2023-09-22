def faltante(lista):
    cont=0
    while cont<len(lista):
        if lista[cont] not in lista:
            return lista[cont]
        cont=cont+1