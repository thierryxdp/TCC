def maiores(lista,n):
    '''dada uma lista de números inteiros e um número inteiro n, retorna
    uma nova lista somente com os números da lista de entrada maiores que n;
    list, int -> list'''

    list.append(lista,n)
    list.sort(lista)
    lugar = list.index(lista,n)+1
    return lista[lugar:] 


def acima_da_media(notas_turma):
    '''dada uma lista com todas as notas de uma turma, retorna uma nova
    lista somente com as notas maiores que a média obtida a partir de 
    todas as notas;
    list -> list'''
    
    media = sum(notas_turma)/len(notas_turma)
    nao_existe = media not in notas_turma

    if nao_existe:
        return maiores(notas_turma,media)
    else:
        list.sort(notas_turma)
        local = list.index(notas_turma,media)+1
        return notas_turma[local:]