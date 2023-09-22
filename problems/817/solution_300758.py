def maiores(lista,num):
    
    list.append(lista,num)
    
    list.sort(lista)
    
    x = list.index(lista,num)
    
    listaFim = lista[x+1:]
    
    return listaFim


def acima_da_media(n):
    
    sm = sum(n)
    
    a = len(n)
    
    md = soma/a
    
    
    if(md in n):
        result = maiores(n,md)
        return result[1:]
    
    else:
        return maiores(n,md)