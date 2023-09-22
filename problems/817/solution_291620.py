def acima_da_media(lista):
    """Funcao que recebe uma lista com as notas dos alunos de uma turma e retorna
    uma lista ordenada com as notas que ficaram acima da media:
    Entrada: list
    Saida: list"""

    media = sum(lista)/len(lista)
    return maiores(lista,media)