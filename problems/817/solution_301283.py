def maiores(ls, n):
    list.append(ls, n)
    list.sort(ls)
    list.reverse(ls)
    indice_de_n = list.index(ls, n)
    ls2 = ls[ :indice_de_n]
    list.sort(ls2)
    return ls2

def acima_da_media(ls):
    """
"""
    media = sum(ls) / len(ls)
    alunos_acima = maiores(ls, media)
    return alunos_acima