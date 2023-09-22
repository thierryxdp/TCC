def acima_da_media(*notas):
    #Essa função dada uma lista com as notas de uma turma
    #Retorna uma lista ordenada comas notas que ficaram acima da média
    media_notas = sum(notas[0])/len(notas[0])
    notas_maiores = []
    for maiores in notas[0]:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return sorted(notas_maiores)