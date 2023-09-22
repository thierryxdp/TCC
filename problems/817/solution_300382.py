def maiores(lista,n):
    ''' Essa função tem como objetivo informar os números inteiros maiores que o número(n) informado, list,int,list'''
    n_lista = [n]
    if n not in lista:
		lista1 = lista+ n_lista
    list.sort(lista1)
    indice = list.index(lista1,n)
    
    return lista1[(indice)+1:]

def acima_da_media(lista):
    ''' Essa função calcula a média de uma lista, voltando os valores acima da media. lista, list'''
    soma = sum(lista)
    
    x = len(lista)
    
    media = (soma/x)
    
    
    return maiores(lista,media)