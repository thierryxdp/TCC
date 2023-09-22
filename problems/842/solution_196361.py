#Start your python function here
def pontost1(jogo):
    if jogo[0][2][0] > jogo[0][2][1]:
  	  	return 3
	if jogo[0][2][0] == jogo[0][2][1]:
  		return 1
    if jogo[0][2][0] < jogo[0][2][1]:
        return 0
def pontost2(jogo):
    if jogo[0][2][0] < jogo[0][2][1]:
  	  	return 3
	if jogo[0][2][0] == jogo[0][2][1]:
  		return 1
    if jogo[0][2][0] > jogo[0][2][1]:
        return 0

def pontos_por_time(jogo):
    return {jogo[0][0]:pontost1(jogo),jogo[0][1]:pontost2(jogo)}