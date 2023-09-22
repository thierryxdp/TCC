def maiores(notas, media):
    """A função recebe uma lista com as notas dos alunos
    e um float correspondente à média entre essas notas e
    retorna outra lista com as notas acima da média em ordem
    crescente."""
    notas_acima = []
    for elemento in notas:
        if elemento > media:
            notas_acima.append(elemento)
            
    list.sort(notas_acima)
    return notas_acima

def acima_da_media(notas_alunos):
    """Recebe como entrada uma lista com as notas dos alunos
    e retorna outra lista com as notas que ficaram acima da média
    em ordem crescente."""
    media = (sum(notas_alunos))/(len(notas_alunos))
    return maiores(notas_alunos, media)