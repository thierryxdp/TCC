def acima_da_media(notas):
    """ função que recebe uma lista com as notas da 
    turma e retorna outra com as acima da média.
    assinatura: list: --> list
    testes:
    acima_da_media([1,6,6,7,10])==[6,6,7,10]
    """
    if len(notas) == 1:
        return []
    media = (sum(notas))/len(notas)
    list.append(notas,media)
    list.sort(notas)
    return ls[list.index(notas,media) + 1:]