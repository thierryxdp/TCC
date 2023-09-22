def faltante(lista):
    list.sort(lista)
    indice=0
    while indice < len(lista):
        if indice != (indice+1):
            return indice+1
        indice=indice+1