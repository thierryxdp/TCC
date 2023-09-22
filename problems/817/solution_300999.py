def acima_da_media(lista):
    '''
    Função que retorna uma lista ordenada com as notas acima da média
    '''
    
    lista1=sum(lista)
    m=int(lista1/len(lista)+1)
    mf=list.append(lista,m)
    list.sort(lista)
    final=lista.index(m)
    
    return lista[final+1:]