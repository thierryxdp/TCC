def acima_da_media(notas):
    #Essa função dada as notas dos alunos de uma turma
    #Retorna uma lista ordenada com as notas que ficaram acima da média
    media_notas = sum(notas)/len(notas)
    notas_maiores = []
    for maiores in notas:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)