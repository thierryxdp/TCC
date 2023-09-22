def jogo(lista):
    
    Cormengo = 0
    Flaminthians = 0

    jogo1 = lista[0]
    pontuacaoJogo1 = jogo1[2]
    
    if pontuacaoJogo1[0] > pontuacaoJogo1[1]:
    	time1 = 3
    	time2 = 0

    if pontuacaoJogo1[0] == pontuacaoJogo1[1]:
    	time1 = 1
    	time2 = 1

    if pontuacaoJogo1[0] < pontuacaoJogo1[1]:
    	time1 = 0
    	time2 = 3


    time3 = 0
    time4 = 0

    jogo2 = lista[1]
    pontuacaoJogo2 = jogo2[2]
    
    if pontuacaoJogo2[0] > pontuacaoJogo2[1]:
    	time3 = 3
    	time4 = 0

    if pontuacaoJogo2[0] == pontuacaoJogo2[1]:
    	time3 = 1
    	time4 = 1

    if pontuacaoJogo2[0] < pontuacaoJogo2[1]:
    	time3 = 0
    	time4 = 3

    pontuacaotime1 = time1 + time4
    pontuacaotime2 = time2 + time3

    return {jogo1[0]:pontuacaotime1,jogo1[1]:pontuacaotime2}