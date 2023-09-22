def maiores(ls):
    """Recebe uma lista com notas de alunos e retorna outra lista, dessa 
    vez com as notas ordenadas de alunos que ficaram acima da média.
    assinatura: list --> list
    testes:
    maiores([2,3,8,9,7]) == [7, 8, 9]
    maiores([7,8,5,2,7]) == [7, 7, 8]
    """
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]