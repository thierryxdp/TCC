def maiores(numeros, n):
    '''Dado uma lista de numeros e um numero n, retorna outra lista com os numeros maiores que n.
    list, int -> list'''
    numeros.append(n)
    numeros.sort()
    pos = numeros.index(n)
    numeros.pop(pos)
    maiores = numeros[pos:]
    return maiores

def acima_da_media(notas):
    '''Dada uma lista de notas, returna uma lista com as notas maiores que a media da turma.
    list -> list'''
    media = sum(notas) / len(notas)
    maiores(notas, media)
    return maiores