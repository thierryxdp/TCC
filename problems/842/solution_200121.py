def pontos_por_time(jogos):
    """Função que recebe duas listas com o nome do time e gols marcados, e resulta nos pontos obtidos por cada time."""
    """Considerando uma vitória por 3 pontos e um empate por 1 ponto"""
    """lista-->dicionário"""
    jogo1=jogos[0]
    jogo2=jogos[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    TimeA=jogo1[0]
    TimeB=jogo1[1]
    Gol1A=placar1[0]
    Gol1B=placar1[1]
    Gol2B=placar2[0]
    Gol2A=placar2[1]
    PA=0
    PB=0
    if Gol1A>Gol1B:
        PA=PA+3
    
    elif Gol1A==Gol1B:
        PA=PA+1 and PB=PB+1
       
    elif Gol1A<Gol1B:
        PB=PB
        
    if Gol2A>Gol2B:
        PA=PA+3
        
    elif Gol2A==Gol2B:
        PA=PA+1 and PB=PB+1
        
    elif Gol2A<Gol2B:
        PB=PB3
    
    Resultado={TimeA:PA,TimeB:PB}
    return Resultado