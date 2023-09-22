def faltante(lista):
    list.sort(lista)
    indice=0
    if len(lista)==lista[indice]:
        return 2
    while indice < len(lista):
        if lista[indice] == indice +1:
            list.sort(lista)
        else:
            return lista[indice] -1
        indice=indice +1
        
    return lista[indice]+1