def maiores(lista,n):
    """Função que dada uma lista e um número inteiro n retorna uma lista nova com somente números maiores que n. list,int --> list"""
    if n not in lista:
        list.append(lista,n)
    
    list.sort(lista)
    indice= list.index(lista,n)
    
    fatiado= lista[indice+1:]
    
    return fatiado