def pontos_por_time(l):
    '''recebe uma lista com informações dos jogos e retorna
    um dicionário com os pontos de cada time
    list -> dict'''
    #organizando as informações antes da competição
    pontos1 = 0
    pontos2 = 0    
    #analisando o primeiro jogo
    jogo1 = l[0]
    if jogo1[2][0] > jogo1[2][1]:
        pontos1+=3
    elif jogo1[2][0] < jogo1[2][1]:
        pontos2+=3
    else:
        pontos1+=1
        pontos2+=1
    #analisando o segundo jogo
    jogo2 = l[1]
    #está na mesma ordem do primeiro jogo
    if jogo2[0] == jogo1[0] and jogo2[1] == jogo1[1]:	
        if jogo2[2][0] > jogo2[2][1]:
            pontos1+=3
        elif jogo2[2][0] < jogo2[2][1]:
            pontos2+=3
        else:
            pontos1+=1
            pontos2+=1
	#inverteu-se a ordem do primeiro jogo            
    else:
        if jogo2[2][0] > jogo2[2][1]:
            pontos2+=3
        elif jogo2[2][0] < jogo2[2][1]:
            pontos1+=3
        else:
            pontos1+=1
            pontos2+=1
	#montando o dicionário
    pontos = {l[0][0]: pontos1, l[0][1]: pontos2}
    return pontos