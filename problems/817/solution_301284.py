def maiores(ls, n):
    list.append(ls, n)
    list.sort(ls)
    list.reverse(ls)
    indice_de_n = list.index(ls, n)
    ls2 = ls[ :indice_de_n]
    list.sort(ls2)
    return ls2

def acima_da_media(ls):
    """Dada uma lista com as notas de alunos
de uma turma, retorna uma lista (ordenada) com as notas
que ficaram acima da média.
assinatura: list --> list
casos de teste:
acima_da_media([2, 4, 6, 8, 10]) == [8, 10]
acima_da_media([2, 4, 6.1, 8, 10]) == [6.1, 8, 10]
acima_da_media([8, 8, 8]) == []
acima_da_media([8, 7.9, 8]) == [8, 8]
"""
    media = sum(ls) / len(ls)
    alunos_acima = maiores(ls, media)
    return alunos_acima