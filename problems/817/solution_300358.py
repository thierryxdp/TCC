def maiores(lista_numero,n):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    list.append(lista_numero, n)
    
    list.sort(lista_numero)
    
    A = list.index(lista_numero,n)
    
    return lista_numero[A+1:]

def acima_da_media(numero):
        
    soma = sum(numero)
    
    x = len(numero)
    
    media = soma/x
    
    
    return int maiores(numero,media))