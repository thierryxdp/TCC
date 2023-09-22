def maiores(lista, n):
    """tendo como parametros uma lista de números inteiros e um número inteiro, a função retorna outra lista, apenas com
    os elementos maiores que n. A lista retornada será em ordem crescente; list, int -> list"""
    listanova = lista + [n]
    list.sort (listanova)
    indexn = list.index(listanova, float(n))
    return listanova[indexn + 1::]

def acima_da_media (lista):
    """tendo como parametros uma lista possuindo as notas de todos os alunos de uma turma, a função
    retorna outra lista, em ordem crescente, com as notas acima da média;lista -> lista"""
    media = sum(lista)/len(lista)
    if len(lista) == 1:
     return []
	else:
     return maiores (lista, media)