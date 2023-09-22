def acima_da_media(x,m):
    '''função que dada uma lista de notas retorna uma lista
    ordenada com as notas acima da média'''
    m=sum(x)/len(x)
    list.append(x,m)
    list.sort(x)
    z=len(x)
    y=list.index(x,m)
    return x[y+1:z]