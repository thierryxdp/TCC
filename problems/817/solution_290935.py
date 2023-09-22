def acima_da_media(lista):
    a=sum(lista)/len(lista)
    lista.append(a)
    list.sort(lista)
    
    if a in lista: 
        
        return lista[lista.index(a)+1:]
    else:
        return lista[lista.index(a)+1:]-lisa[0]