def acima_da_media (lista):
    """Função que recebe uma lista com as notas dos alunos e retorna as notas que ficaram acima da media; lista -> lista"""
    x = sum(lista)
    y = len(lista)
    media = x/y
    notas = lista[] >= media
    return notas