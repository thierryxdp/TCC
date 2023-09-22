def pontos_por_time(jogo):
    '''Retorna um dicionario com o nome do time e a quantidade de pontos que ele possui
    list->dict'''
   
    if 'Cormengo'==jogo[0][0]:
        saldoGolsC1=jogo[0][2][0]
        saldoGolsF1=jogo[0][2][1]
    else:
        saldoGolsF1=jogo[0][2][0]
        saldoGolsC1=jogo[0][2][1]
        
    if 'Cormengo'==jogo[1][0]:
        saldoGolsC2=jogo[1][2][0]
        saldoGolsF2=jogo[1][2][1]
    else:
        saldoGolsF2=jogo[1][2][0]
        saldoGolsC2=jogo[1][2][1]
        
    if saldoGolsC1==saldoGolsF1:
        pontosCormengo=1
        pontosFlaminthians=1
    elif saldoGolsC1>saldoGolsF1:
        pontosCormengo=3
        pontosFlaminthians=0
    else:
        pontosCormengo=0
        pontosFlaminthians=3
        
    if saldoGolsC2==saldoGolsF2:
        pontosCormengo+=1
        pontosFlaminthians+=1
    elif saldoGolsC2>saldoGolsF2:
        pontosCormengo+=3
        pontosFlaminthians+=0
    else:
        pontosCormengo+=0
        pontosFlaminthians+=3
        
	return {'Cormengo':pontosCormengo,'Flamínthians':pontosFlaminthians}