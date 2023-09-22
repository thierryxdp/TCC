def acima_da_media(notas):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas acima da média;
    list -> list"""
    lnotas = [notas]
    snotas = sum(lnotas)
    mnotas = snotas/len(lnotas)
    nmaiores = [i for i in notas if i>n]
    return sorted(nmaiores, key=int)