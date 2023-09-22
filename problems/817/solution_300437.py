def maiores(lista_numero,n):
    
    if n in lista_numero:
        return lista_numero
    
    elif n not in lista_numero:
        list.append(lista_numero, n)
    
    list.sort(lista_numero)
    
    A = list.index(lista_numero,n)
    
    return lista_numero[A+1:]


def acima_da_media(numero):
    
    
    
    soma = sum(numero)
    
    x = len(numero)
    
    media = soma/x
    
    resultado = maiores(numero,media)

    return resultado