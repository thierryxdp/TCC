def acima_da_media(notas):
    """Função que recebe uma lista com as notas dos alunos e retorna outra lista
com as notas que estiverem acima da média.
    list -> list"""

    a = (sum(notas))/(len(notas))
    b = maiores(notas,a)

    return b