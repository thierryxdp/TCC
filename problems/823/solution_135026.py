def faltante(lista):
    list.sort(lista)
    indice=1
    while indice <= len(lista):
        if indice != lista[indice-1]:
            return lista[indice]
        indice=indice+1