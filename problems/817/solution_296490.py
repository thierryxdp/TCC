def maiores(lista, n):
    """tendo como parametros uma lista de números inteiros e um número inteiro n, a função retorna outra lista, apenas com
    os elementos maiores que n. A lista retornada será em ordem crescente; list, int -> list"""
    listanova = lista + [n]
    list.sort (listanova)
    indexn = list.index(listanova, n)
    numerosdevezesn = list.count(lista,n)
    return listanova[indexn + numerosdevezesn::]

def acima_da_media (lista):
    """tendo como parametros uma lista possuindo as notas de todos os alunos de uma turma, a função
    retorna outra lista, em ordem crescente, com as notas acima da média;list -> list"""
    media = sum(lista)/len(lista)
    listaordenada = maiores (lista, media)
    if len(lista) == 1:
        return []
    else:
		return listaordenada