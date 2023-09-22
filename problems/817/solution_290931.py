def acima_da_media(lista):
    a=sum(lista)/len(lista)
    lista.append(a)
    list.sort(lista)
    
    if int(a) in lista: 
        
        return lista[lista.index(a)+2:]
    else:
        return lista[lista.index(a)+1:]