def maiores(lista_numeros,n):
    """funcao que, dado uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista, a qual contenha todos os numeros da lista original maiores que n;
    list, int -> list"""
    lista_manipulavel=lista_numeros[:]
    lista_manipulavel+=[n]
    lista_manipulavel.sort()
    list.reverse(lista_manipulavel)
    indice=list.index(lista_manipulavel,n)
    lista_manipulavel=lista_manipulavel[:indice]
    lista_manipulavel.sort()
    return lista_manipulavel

def acima_da_media(lista):
    """funcao que, dada uma lista com notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da media;
    list -> list"""
    media=(sum(lista))/(len(lista))
    return maiores(lista,media)