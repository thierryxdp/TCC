def pontos_por_time(jogos):
    """Função que recebe duas listas com o nome do time e gols marcados, e resulta nos pontos obtidos por cada time."""
    """Considerando uma vitória por 3 pontos e um empate por 1 ponto"""
    """lista-->dicionário"""
    TimeA=jogos[0]
    TimeB=jogos[1]
    Gol1A=jogos[2]
    Gol1B=jogos[3]
    Gol2B=jogos[6]
    Gol2A=jogos[7]
    PA=()
    PB=()
    if Gol1A>Gol1B:
        PA+3
    
    elif Gol1A==Gol1B:
        PA+1 and PB+1
       
    elif Gol1A<Gol1B:
        PB+3
        
    if Gol2A>Gol2B:
        PA+3
        
    elif Gol2A==Gol2B:
        PA+1 and PB+1
        
    elif Gol2A<Gol2B:
        PB+3
    
    Resultado={TimeA:PA,TimeB:PB}
    return Resultado