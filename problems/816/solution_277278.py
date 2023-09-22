def acima_da_media (lista, x):
    """Função que recebe uma lista com as notas dos alunos e retorna as notas que ficaram acima da media; lista -> lista"""
    z = ([n for n in lista if n > lista])
    return sorted(z)