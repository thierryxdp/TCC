def media(notas):
    ''' Função que dada uma lista de números inteiros e um número inteiro , retorna outra lista que contenha todos os númros da lista riginal maiores que n
    lista, int->list'''
  
    posicao=list.index(notas,n)
    return notas[posicao+1:]

        

def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas que ficaram acima da média'''
    posicao=sum(notas)/len(notas)
    media=notas[posicao+1:]
    return media