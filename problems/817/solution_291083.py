def acima_da_media(lista):
    """Retorna uma lista ordenada com todas as notas acima da média.
    lista -> lista"""
    
    soma=sum(lista)
    quantidade=len(lista)
    media=soma/quantidade
    
    list.append(lista,media)
    list.sort(lista)
    a=list.index(lista,media)
    
    if float(lista[a-1])==float(lista[a]):
        del lista[a-1]
        
    if float(lista[a+1])==float(lista[a]):
        del lista[a+1]
        
    return lista[a+1:]