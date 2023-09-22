def acima_da_media(*notas):
    #Essa função dada uma lista com as notas de uma turma
    #Retorna uma lista ordenada comas notas que ficaram acima da média
    media_notas = sum(notas)/len(notas)
    notas_maiores = []
    for maiores in notas:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)