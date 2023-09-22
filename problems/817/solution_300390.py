def maiores(lista,n):
    ''' Essa função tem como objetivo informar os números inteiros maiores que o número(n) informado, list,int,list'''
    if n not in lista:
    	list.append(n)
    list.sort(lista)
    indice = list.index(lista,n)
    
    return lista[(indice)+1:]

def acima_da_media(lista):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    soma = sum(lista)
    
    x = len(lista)
    
    media = (soma/x)
    
    
    return maiores(lista,media)