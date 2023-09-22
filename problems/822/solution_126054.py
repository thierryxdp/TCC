def repetidos(lista_num):
    indice=1
    resultado=0
    while indice<=len(lista_num):
        if lista_num[indice]//lista_num[indice-1]==1:
            resultado = resultado+1                       
        indice = indice + 1
    return resultado