def acima_da_media(notas):
    """Função que, dada uma lista com as notas de todos os alunos de uma sala,
    retorna uma lista ordenada somente com as que ficaram acima da média
    list -> list"""
    m=(sum(notas))/len(notas)
    acima=maiores(notas,m)
    return acima