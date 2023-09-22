def maiores(lista_num,n):
    lista_num+[n]
    list.sort(lista_num)
    posiçao = list.index(lista_num,n)
    
    
    return lista_num[posiçao:]