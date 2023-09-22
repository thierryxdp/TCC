def acima_da_media(lista):
    '''retorna uma lista ordenada com as notas que ficaram acima da media'''
    '''list ->list'''
    
    a=sum(lista)
    b=len(lista)
    c=a//b
    list.append(lista,c)
    list.sort(lista)
    list.reverse(lista)
    d=list.index(lista,c)
    e=lista[0:d]
    list.sort(e)
    
    return e