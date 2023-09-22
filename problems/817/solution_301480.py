def acima_da_media(ls):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista em ordem crescente somente com as notas que
fora aprovadas.
assinatura: list -> list
acima_da_media([2, 5, 4, 6, 3, 10, 9, 9]) == [6.0, 9, 9, 10]
acima_da_media([1, 1, 6, 9, 10]) == [6, 9, 10]
"""
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]