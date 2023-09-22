def pontos_por_time(Lista1):
    '''Função que retorna a quantidade de pontos de um time em dois jogos de um campeonato
    Parâmetros de Entrada:List, List
    Valor de Saída: Dicionário'''
    
    Time1 = (Lista1[0])[0]
    Time2 = (Lista1[0])[1]
    Jogo1 = (Lista1[0])[2]
    Jogo2 = (Lista1[1])[2]
    
 if Jogo1[0] == Jogo1[1]:
        Pontuacao11 = 1
        Pontuacao21 = 1
    elif Jogo1[0] > Jogo1[1]:
        Pontuacao11 = 3
        Pontuacao21 = 0
    else:
        Pontuacao11 = 0
        Pontuacao21 = 3
        
 if Jogo2[0] == Jogo2[1]
    	Pontuacao12 = 1
        Pontuacao22 = 1
    elif Jogo2[0] > Jogo2[1]:
        Pontuacao12 = 0
        Pontuacao22 = 3
    else:
        Pntuacao12 = 3
        Pontuacao22 = 0
        
        return {Time1: (Pontuacao11 + Pontuacao12), Time2: (pontuacao21 + Pontuacao22)}