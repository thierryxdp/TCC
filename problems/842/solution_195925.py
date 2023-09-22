def pontos_por_time(confronto_idaevolta):
    '''Função que recebe 1 lista com 2 elementos que também são 2 listas.
    A lista completa tem informações do número de gols em dois jogos de
    futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato:
    [[’Cormengo’,’Flamínthians’, [1, 0]], [’Flamínthians’, ’Cormengo’, [2, 2]]]. 
    A função irá retornar um dicionário cujos mapeamentos são:<nome do time> → <número de pontos na fase>.
    Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, os times recebem três pontos
	por vitória e um ponto por empate. Não são atribuídos pontos para derrotas. lista->dicionário'''
    if confronto_idaevolta[0][2][0]>confronto_idaevolta[0][2][1]:
        ptsCormengo_1=3
        ptsFlaminthians_1=0
    elif confronto_idaevolta[0][2][0]<confronto_idaevolta[0][2][1]:
        ptsCormengo_1=0
        ptsFlaminthians_1=3
    elif confronto_idaevolta[0][2][0]=confronto_idaevolta[0][2][1]:
        ptsCormengo_1=1
        ptsFlaminthians_1=1
    if confronto_idaevolta[1][2][0]>confronto_idaevolta[1][2][1]:
        ptsCormengo_2=0
        ptsFlaminthians_2=3
    elif confronto_idaevolta[1][2][0]<confronto_idaevolta[1][2][1]:
        ptsCormengo_2=3
        ptsFlaminthians_2=0
    elif confronto_idaevolta[1][2][0]=confronto_idaevolta[1][2][1]:
        ptsCormengo_2=1
        ptsFlaminthians_2=1
    return {'Cormengo':ptsCormengo_1+ptsCormengo_2,'Flamínthians':ptsFlaminthians_1+ptsFlaminthians_2}