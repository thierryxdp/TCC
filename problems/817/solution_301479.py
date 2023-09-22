def acima_da_media(ls):
    """Recebe uma lista com notas de alunos e retorna outra lista, dessa 
    vez com as notas ordenadas de alunos que ficaram acima da média.
    assinatura: list --> list
    testes:
    acima_da_media([5,6,7,8,9]) == [7, 8, 9]
    acima_da_media([5,1,6,8,9]) == [6, 8, 9]
    """
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]