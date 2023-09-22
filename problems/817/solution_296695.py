def acima_da_media(lista):
    '''retorna uma lista ordenada com as notas que ficaram acima da media'''
    '''list ->list'''
    list.sort(lista)
    a=sum(lista)
    b=len(lista)
    c=a//b
    d=list.index(lista,c)
    
    return lista[d:]