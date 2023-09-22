def maiores(lista, n):
    '''ao receber uma lista de números inteiros
    e um número inteiro n, retorna um lista contendo
    apenas os elementos maiores que o número n inserido.
    list, int -> list'''
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    del lista[:indice+1]
    return lista

def acima_da_media(notas):
    '''ao receber uma lista com as notas dos alunos de
    uma turma, retorna uma lista ordenada com as notas
    que ficaram acima da média geral.
    list -> list'''
    media = sum(notas) / len(notas)
    if media in notas:
        list.remove(notas, media)
        notas = maiores(notas, media)
        return notas
    else:
        notas = maiores(notas, media)
        return notas