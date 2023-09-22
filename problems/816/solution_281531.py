def maiores(numeros, n):
    '''Funcao recebe uma lista contendo numeros interios e um numero qualquer e retoena os numeros que são maiores que esse outro numero qualquerr
Lista/int -> Lista'''
    listaN = (numeros + [n])
    list.sort(listaN)
    posicao = list.index(listaN, n)
    return listaN[posicao+1:]