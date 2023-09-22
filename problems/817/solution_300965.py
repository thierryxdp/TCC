def acima_da_media(lista):
    
    
    x=sum(lista)/len(lista)
    list.append(lista,x)
    list.sort(lista)
    
    z=list.index(lista,x)
    del lista[x]
    
    return lista[z+1:]