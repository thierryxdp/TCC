def acima_da_media (notas):
    """ funcao ira receber uma lista com as notas dos alunos e retornara a media da turma e uma lista ordenada com as notas que ficaram acima da media
    list -> float,list"""
    media_turma = sum(notas) / len (notas)
    list.append (notas,media_turma)
    list.sort (notas)
    resultado_notas = notas[ : list.index(notas,media_turma) : -1 ]
    if media_turma in resultado_notas:
        list.remove ( resultado_notas, media_turma)
    list.sort (resultado_notas)
    return media_turma , resultado_notas