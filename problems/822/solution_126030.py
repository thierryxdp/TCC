def repetidos(lista_num):
    indice=1
    resultado=''
    while indice<=len(lista_num):
        if lista_num[indice] == lista_num[indice-1]:
            lista_num = lista_num + [lista_num[indice]]                        
        indice = indice + 1
    return len(lista_num)