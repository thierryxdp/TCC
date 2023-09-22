def acima_da_media(notas):
    """funcao que recebe uma lista com as notas de todos os alunos e retorna uma lista ordenada com as notas que ficaram acima da media;
    list->float,list"""
    media_turma = sum(notas) / len(notas)
    list.append (notas, media_turma)
    list.sort (notas)
    resultado_notas = notas[: list.index(notas, media_turma) : -1 ]
     if media_turma in resultado_notas:
        list.remove (resultado_notas, media_turma)
        list.sort (resultado_notas)
        return resultado_notas