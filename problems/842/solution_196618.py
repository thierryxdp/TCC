def pontostime1ida(jogo):
    if jogo[0][2][0] > jogo[0][2][1]:
    	return 3
    if jogo[0][2][0] == jogo[0][2][1]:
    	return 1
    if jogo[0][2][0] < jogo[0][2][1]:
    	return 0
def pontostime1volta(jogo):
   	if jogo[1][2][0] > jogo[1][2][1]:
    	return 3
   	if jogo[1][2][0] == jogo[1][2][1]:
    	return 1
	if jogo[1][2][0] < jogo[1][2][1]:
    	return 0

def pontost1(jogo):
    return pontostime1ida(jogo)+pontostime1(volta)

def pontostime2ida(jogo):
    if jogo[0][2][1] > jogo[0][2][0]:
    	return 3
    if jogo[0][2][1] == jogo[0][2][0]:
    	return 1
    if jogo[0][2][1] < jogo[0][2][0]:
    	return 0
def pontostime2volta(jogo)
   if jogo[1][2][1] > jogo[1][2][0]:
    	return 3
    if jogo[1][2][1] == jogo[1][2][0]:
    	return 1
    if jogo[1][2][1] < jogo[1][2][0]:
    	return 0
def pontost2(jogo):
    return pontostime2ida(jogo)+pontostime2volta(jogo)

def pontos_por_time(jogo):
	return{jogo[0][0]:pontost1,jogo[0][1]:pontost2}