def acima_da_media(notas):
    #Essa função dada as médias dos alunos
    #Retorna uma lista ordenada com as notas que ficaram acima da média
    media_notas = sum(int(notas))/len(int(notas))
    notas_maiores = []
    for maiores in notas[int]:
        if maiores > media_notas:
            notas_maiores.append(maiores)
            return media_notas, sorted(notas_maiores)