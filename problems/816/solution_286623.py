def acima_da_media(ls):
    """Recebe uma lista com notas de alunos e retorna outra lista, dessa 
    vez com as notas ordenadas de alunos que ficaram acima da média.
    assinatura: list --> list
    testes:
    acima_da_media([4,5,2,7,9]) == [7, 9]
    acima_da_media([2,3,8,9,7]) == [7, 8, 9]
    """
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]