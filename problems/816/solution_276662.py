def maiores(lista_numero, n):
    
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    
    posicao = list.index(lista_numero,n)
    
    return lista_numero[posicao+1:]