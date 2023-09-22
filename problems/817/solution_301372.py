def acima_da_media(ls):
    """Fução que dada uma lista com as notas dos alunso de uma turma, retorna uma lista em ordem crescente somente com as notas que
fora aprovadas.
list -> list
acima_da_media([1,2,3,4,5,6,7,8,9,10]) == [6, 7, 8, 9, 10]
acima_da_media([1,9,0,3]) == [9]
"""
    if len(ls) == 1:
        return []
    media = (sum(ls))/len(ls)
    list.append(ls,media)
    list.sort(ls)
    return ls[list.index(ls,media) + 1:]