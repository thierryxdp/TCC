def acima_da_media(notas):
    """Funcao que recebe as notas dos alunos de uma turma e retorna a meida da turma
    e uma lista ordenada com as notas que ficaram acima da media."""
    somaNotas = sum(notas)
    qtdNotas = len(notas)
    media = somaNotas/qtdNotas
    media = round(media,0)
   
    return media