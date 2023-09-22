def maiores(lista_numero,n):
    
    list.append(lista_numero, n)
    
    list.sort(lista_numero)
    
    A = list.index(lista_numero,n)
    
    return lista_numero[A+1:]


def acima_da_media(numero):
    
    soma = sum(numero)
    
    x = len(numero)
    
    media = soma/x
    
    if x = 1:
        return []
    
    else:
    return maiores(numero,media)