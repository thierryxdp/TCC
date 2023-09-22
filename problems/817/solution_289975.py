def media(lista,notas):
    ''' Função que dada uma lista de números inteiros e um número inteiro , retorna outra lista que contenha todos os númros da lista riginal maiores que n
    lista, int->list'''
    list.append(lista,notas)
    list.sort(lista)
    posicao=list.index(lista,notas)
    return lista[posicao+1:]

        

def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média'''
    notas=sum(notas)/len(notas)
    media(lista,notas)
    return notas