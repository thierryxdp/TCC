def acima_da_media(lista):
    a=sum(lista)/len(lista)
    lista.append(a)
    list.sort(lista)
    
    if a==lista[lista.index(a)+1]:
        
        x=lista[lista.index(a)+1:]
        return x
        
        
    else:
        return lista[lista.index(a)+1:]