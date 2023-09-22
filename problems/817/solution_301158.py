def acima_da_media(lista):
    x=sum(lista)/len(lista)
 
    list.append(lista,x)
    list.sort(lista)
    del lista[:x+1]
    return lista