def maiores(lista_num,n):
    lista = lista_num+[n]
    list.sort(lista)
    posicao = list.index(lista,n)
    
    
    return lista[posicao:]