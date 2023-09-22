def acima_da_media(notas):
    """Funcao que, dada uma lista com as notas de alunos de uma turma, 
    retorna a média da turma e uma lista ordenada com as notas que 
    ficaram acima da média."""
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return media_notas, maiores_notas