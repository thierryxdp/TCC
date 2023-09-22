def maiores(lista,n):
    '''função que retorna uma lista em ordem crescente
    dos números maiores que n
    valor de entrada: list, int
    valor de saída: list'''
    lista.append(n)
    lista.sort()
    crescente= lista[lista.index(n)+1:]
    return crescente

def acima_da_media(lista):
    '''função que retorna as notas que ficaram acima da média 
    em uma lista crescente
    valor de entrada:list
    valor de saída: list'''
    media= (sum(lista))/(len(lista))
    return maiores(lista,media)