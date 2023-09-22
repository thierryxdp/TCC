def pontos_por_time(placares):
    '''função que recebe como parâmetro uma lista "placares", cujos 2 únicos
elementos são duas listas, em que cada lista contém uma string contendo
o nome do time da casa, outra string contendo o nome do time visitante, e o
terceiro elemento é uma lista com o número de gols de cada time; retorna
um dicionário com 2 mapeamentos, onde as chaves são os nomes dos times(string)
e o valor representa o número de pontos do time; list->dict'''
    
    [timeA,timeB,[golAi,golBi]]=placares[0]
    [timeB,timeA,[golBv,golAv]]=placares[1]

    pontosAi= 3*int(golAi>golBi) + int(golAi==golBi)
    pontosBi= 3*int(golAi<golBi) + int(golAi==golBi)
    pontosAv= 3*int(golAv>golBv) + int(golAv==golBv)
    pontosBv= 3*int(golAv<golBv) + int(golAv==golBv)

    return {timeA:pontosAi+pontosAv,timeB:pontosBi+pontosBv}