def maiores(numeros,n):
    '''Recebe uma lista e um elemento n e retorna uma nova lista com
    todos os elementos maiores do que n (list, int -> int)'''
    list.append(numeros,n)
    list.sort(numeros)
    posicao_n = numeros.index(n)
    return numeros[posicao_n + 1 : ]
def acima_da_media (notas):
    '''R'''
    media = sum(notas)/len(notas)
    maiores(notas,media)
    return notas[posicao_n + 1 :]