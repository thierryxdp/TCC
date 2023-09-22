def pontos_por_time (jogo):
    """Função que me dado uma lista com jogos de time e ida, retorna para mim a quantidade de pontos obtidos pelos times 
dentro de um dicionario. list.list>bool"""
    
    time1=jogo[0][0]
    time2=jogo[0][1]
    jogo1=jogo[0][2]
    jogo2=jogo[1][2]
    
    if jogo1[0]==jogo[1]:
        pontuacao1=1
        pontuacao2=1
    elif jogo1[0]>jogo1[1]:
        pontuacao1=3
        pontuacao2=0
    else:
        pontuacao1=0
        pontuacao2=3
    if jogo2[0]==jogo2[1]:
        pontuacao3=1
        pontuacao4=1
    elif jogo2[0]>jogo2[1]:
        pontuacao3=0
        pontuacao4=3
    else:
        pontuacao3=3
        pontuacao4=0
    return {time1:(pontuacao1+pontuacao3), time2:(pontuacao2+pontuacao4)}