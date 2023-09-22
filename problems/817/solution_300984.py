def acima_da_media(lista):
    
    
    x=sum(lista)/len(lista)
    x=int(x)
    list.append(lista,x)
    list.sort(lista)
    
    z=list.index(lista,x)
    del lista[0:z+1]
    
    if z==x:
        return lista[z+1:]
    
    else:
        return lista