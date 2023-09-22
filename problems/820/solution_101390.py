def posLetra(lista_num):
    lista_num=[]
    indice=0
    while indice<len(lista_num):
        if lista_num[indice] == lista_num[indice-1] or lista_num[indice] == lista_num[indice+1]:
            list.count(lista_num, lista_num[indice])
        indice=indice+1
    return lista_num