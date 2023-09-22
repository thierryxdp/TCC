def acima_da_media(notas):
    #Essa função dada as médias dos alunos
    #Retorna uma lista ordenada com as notas que ficaram acima da média
    media_notas = sum(notas)/len(notas)
    for maiores in notas:
        maiores_notas = maiores(notas,media_notas)
        if maiores > media_notas:
            return media_notas, sorted(notas_maiores)