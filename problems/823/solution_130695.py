def faltante(lista):
    indice=0
    while indice<len(lista):
        if lista[indice]+1==lista[indice+1]:
            indice=indice+1
        else:
            return lista[indice]+1