def maiores(lista_numero,n):
    
    if n in lista numeros:
        Return lista numeros
        
    elif n not in lista numeros:
        Return list.append(lista_numero, n)
    
    list.sort(lista_numero)
    
    A = list.index(lista_numero,n)
    
    return lista_numero[A+1:]


def acima_da_media(numero):
    
    soma = sum(numero)
    
    x = len(numero)
    
    media = soma/x
    

    return maiores(numero,media)