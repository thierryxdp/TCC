def acima_da_media(lista):
    
    
    x=sum(lista)/len(lista)
    list.append(lista,x)
    list.sort(lista)
    
    z=list.index(lista,x)
    del lista[0:z+1]
    
    if [z] in list:
        del lista[z]
        return lista
    
    else:
        return lista