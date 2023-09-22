def maiores(lista,num):
    list.append(lista,num)
    list.sort(lista)
    x = list.index(lista,num)
    listaFim = lista[x+1:]
    return listaFim

def acima_da_media(num):
    soma = sum(num)
    a = len(num)
    md = soma/a
        
    if(media in num):
        result = maiores(num,md)
        return result[1:]
    
    else:
        return maiores(num,md)