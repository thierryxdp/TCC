def acima_de_media(notas):
    """função que dada uma lista com as notas de aluno de uma
    turma, retornaa media da turma e uma lista ordenada com 
    as notas que ficam acima da media. entrada:
    lista(int); saida: lista(int)"""
    mediaNotas= sum(notas)/len(notas)
    maioresNotas= maiores(notas,media_notas)
    return maioresNotas