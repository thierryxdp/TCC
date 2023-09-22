def maiores(lista,n):
    """Dada uma lista e de números inteiros e um número inteiro n, retorna uma lista com todos os elementos
    da lista original maiores que n.
    lista, int/float -> lista"""
    lista = lista+[n]
    list.sort(lista)
    indice=list.index(lista,n)
    sublista=lista[indice+1:]
    rep = list.count(sublista,n)
    if rep != 0:
        sublista = sublista[rep: ]
    return sublista

def acima_da_media(notas):
    """ Dada uma lista com notas de alunos de uma turma , retorne uma lista 
    ordenada com as notas que ficaram acima da média.
    list -> tup"""
    media=sum(notas)/len(notas)
    return media, maiores(notas,media)