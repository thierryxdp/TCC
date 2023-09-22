def acimaDaMedia(notas):
    """função que recebe uma lista com as notas dos alunos de uma turma e retorna
    uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    media = sum(notas)/len(notas)
    return maiores(notas, media)