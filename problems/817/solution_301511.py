def acima_da_media(ls):
    """Recebe uma lista com notas de alunos e retorna outra 
    lista, com as notas ordenadas dos alunos que ficaram acima
    da média.
    assinatura: list --> list
    testes:
    acima_da_media([2,6,9,10]) == [9,10]
    acima_da_media([4,6,8,10]) == [8,10]
    """
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]