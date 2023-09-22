def maiores(lista, n):
    '''Função que retorna uma lista com todos os números maiores que o numero n na lista
    dos inteiros.
    inteiros -> list
    n -> int
    return -> list'''

    lista_ordenada = lista
    

    lista.append(n)
    lista.sort()
    posicao = lista_ordenada.index(n)

    return lista_ordenada[posicao+1:]








def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com a nota de todos os alunos
    que ficaram  acima da média, dada uma lista com as notas.
    lista - > list
    return -> list'''