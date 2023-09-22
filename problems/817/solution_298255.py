def acima_da_media(lista):
    """ii"""
  
    
    b=int(len(lista))
    c=sum(lista)
    m=c/b
    lista.append(m)
    list.sort(lista)
    a=int(lista.index(m))+1
    d=lista.count(m)
    
    if b==1:
        return []
    else:
        return lista[a:]