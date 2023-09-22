def maiores(lista_num, n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num[ lista_num.index(n)+1: ]

def acima_da_media(lista_notas):
    """
    Retorna os alunos acima da media baseado na (lista_notas)
    list -> list
    """
    media = sum(lista_notas) / len(lista_notas)
    ret = maiores(lista_notas, media)
    if len(ret) < 1:
        ret = []
    return ret