def pontos_por_time(listaX):
	"""Declare uma lista de dois elementos, onde cada elmento é uma lista. A primeira lista deve conter os nomes dos times que disputam uma partida de futebol e a segunda lista o numero de gols de cada time"""
    jogoDaIda = listaX[0]
    jogoDaVolta = listaX[1]
    timeA = jogoIda[0]
    timeB = jogoIda[1]
    placarA = jogoIda[2]
    placarB = jogoVolta[2]
    pontuacaoTimeAJGA = placarA[0]
    pontuacaoTimeBJGB = placarA[1]
    pontuacaoTimeBJGB = placarB[1]
    pontuacaoTimeBJGB = placarB[0]
    if pontuacaoTimeAJGA > pontuacaoTimeBJGA:
        pontuacaoTA = 3
        pontuacaoTB = 0
    elif pontuacaoTimeAJGA < pontuacaoTimeBJGA:
        pontuacaoTA = 0
        pontuacaoTB = 3
    elif pontuacaoTimeAJGA == pontuacaoTime2JG1:
        pontuacaoT1 = 1
        pontuacaoT2 = 1
if pontuacaoTimeAJGB > pontuacaoTimeBJGB:
        pontuacaoTA = pontuacaoTA + 3
        pontuacaoTB = pontuacaoTB + 0
    elif pontuacaoTimeAJGB < pontosTimeBJGB:
        pontuacaoTA = pontuacaoTA + 0
        pontuacaoTB = pontuacaoTB + 3
    elif pontosTimeAJGB == pontosTimeBJGB:
        pontuacaoTA = pontuacaoTA + 1
        pontuacaoTB = pontuacaoTB + 1
    return {timeA:pontuacaoTA , timeB:pontuacaoTB}