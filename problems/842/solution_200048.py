def pontos_por_time(lista):
 'Essa função calcula os pontos de dois times dados os seus jogos'
jogo1 = lista[0]
jogo2 = lista[1]
pontos1 = jogo1[2]
pontos2 = jogo2[2]
if (pontos1[0] + pontos2[1]) > (pontos1[1] + pontos2[0]):
    dicionario = {'nome do time':jogo1[0],'numero total de pontos na fase':(pontos1[0] + pontos2[1]),'nome do time':jogo1[1],'numero total de pontos na fase':(pontos1[1] + pontos2[0])}
    return dicionario