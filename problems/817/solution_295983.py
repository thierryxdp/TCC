def maiores(lista_int, n):
    '''Dada uma lista de números inteiros e um inteiro n,
    retorna outra lista contendo todos os números da lista
    original maiores que n ordenados na ordem crescente
    list, int -> list'''
    lista_int = lista_int + [n]
    list.sort(lista_int)
    pos_n = list.index(lista_int, n)
    lista_int = lista_int[pos_n + 1:]
    return lista_int

def acima_da_media(notas):
    '''Dada uma lista com as notas dos alunos da turma,
    retorna uma lista ordenada com as notas que ficaram
    acima da média
    list -> list'''
    media = sum(notas) / len(notas)
    if len(notas) > 1:
        return maiores(notas, media)
    elif media in notas:
        return maiores(notas, media)[1:]
    else:
        return []