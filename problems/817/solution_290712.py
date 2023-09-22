def acima_da_media(notas):
    #Essa função dada as médias dos alunos
    #Retorna uma lista ordenada com as notas que ficaram acima da média
    media_notas = sum(notas[0])/len(notas[0])
    notas_maiores = []
    for maiores in notas[0]:
        if maiores > media_notas:
            notas_maiores.append(maiores)
            return media_notas, sorted(notas_maiores)