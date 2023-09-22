def faltante(lista):
    indice=0
    while indice<len(lista):
        if lista[indice]==lista[indice+1]:
            indice=indice+1
        else:
            return lista[indice]+1