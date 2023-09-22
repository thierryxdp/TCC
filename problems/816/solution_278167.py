def maiores(lista,num):
    """..."""
    list.append(lista,num)
    list.sort(lista)
    
    posicao_aparicao = list.index(lista,num)
    
    return lista[posicao_aparicao+1:]