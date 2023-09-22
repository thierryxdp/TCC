def maiores(lista_num,n):
    lista_num+[n]
    list.sort(lista_num)
    posicao = list.index(lista_num,n)
    
    
    return lista_num[posicao:]