def acima_da_media(notas):
    #Essa função dada as notas dos alunos de uma turma
    #Retorna uma lista ordenada com as notas que ficaram acima da média
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return media_notas, maiores_notas