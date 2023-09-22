def pontos_por_time (informacoes):
    """função que retorna os times e suas pontuações em uma fase"""
    """lista -> dicionário"""
    time_A = informacoes [0][0]
    time_B = informacoes [0][1]
    pontos_time_A_casa = informacoes [0][2][0]
    pontos_time_B_fora = informacoes [0][2][1]
    pontos_time_A_fora = informacoes [1][2][1]
    pontos_time_B_casa = informacoes [1][2][0]
    
    pontuacao_A = 0
    pontuacao_B = 0
    
    if pontos_time_A_casa > pontos_time_B_fora:
        pontuacao_A = pontuacao_A + 3
    
    if pontos_time_A_casa < pontos_time_B_fora:
        pontuacao_B = pontuacao_B + 3
    
    if pontos_time_B_casa > pontos_time_A_fora:
        pontuacao_B = pontuacao_B + 3
    
    if pontos_time_B_fora < pontos_time_A_casa:
        pontuacao_A = pontuacao_A + 3
        
    if pontos_time_A_casa == pontos_time_B_fora or pontos_time_A_fora == pontos_time_B_casa:
        pontuacao_A = pontuacao_A + 1
        pontuacao_B = pontuacao_B + 1
        
    return {time_A:pontuacao_A,time_B:pontuacao_B} or {time_B:pontuacao_B,time_A:pontuacao_A}