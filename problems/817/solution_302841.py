def maiores(numeros,n):
    '''Recebe uma lista e um elemento n e retorna uma nova lista com
    todos os elementos maiores do que n (list, int -> int)'''
    list.append(numeros,n)
    list.sort(numeros)
    posicao_n = numeros.index(n)
    return numeros[posicao_n + 1 : ]
def acima_da_media (notas):
    '''R'''
    if len(notas) > 1
    media = sum(notas)/len(notas)
    return maiores(notas,media)
    else:
        return []