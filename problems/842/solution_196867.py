def pontos_por_time(lista):
    lista1=lista[0]#referente aos times
    lista2=lista[1]#referente aos pontos
    if lista2[0]>lista2[1] or lista2[0]<lista2[1]:
        return {lista1[0]:lista2[0]*3,lista1[1]:lista2[1]*3}
    else:
        return {lista1[0]:lista2[0],lista1[1]:lista2[1]}