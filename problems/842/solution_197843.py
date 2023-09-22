def pontos_por_time (jogo):
    """Função que me dado uma lista com jogos de time e ida, retorna para mim a quantidade de pontos obtidos pelos times 
dentro de um dicionario. list.list>bool"""
    
    if jogo[0][2][0]>jogo[0][2][1]:
        t1=3
        t2=0
    elif jogo[0][2][0]<jogo[0][2][1]:
        t1=0
        t2=3
    else:
        t1=1
        t2=1
    if jogo[1][2][0]>jogo[1][2][1]:
        t1=t1+0
        t2=t2+3
    elif jogo[1][2][0]<jogo[1][2][1]:
        t1=t1+3
        t2=t2+0
    else:
        t1=t1+1
        t2=t2+1
    return {jogo[0][0]:t1, jogo[0][1]:t2}