def acima_da_media(lista):
    
    lista1=sum(lista)
    m=int(lista1/len(lista)+1)
    mf=list.append(lista,m)
    list.sort(lista)
    final=lista.index(mf)
    
    return lista[final+1:]