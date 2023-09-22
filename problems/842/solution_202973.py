# Essa função recebe uma lista com dois elementos que também são listas.
# Dentro de cada elemento, estão os dois times e mais uma lista com a pontuação deles
# A função calcula a pontuação de cada time (empate: 1pt p/ cada; vitória: 3pts p/ vencedor; derrota: 0pts p/ perdedor)
# Ela retorna um dicionário com os pontos finais de cada jogador

# list -> dict

def pontos_por_time(listas_jogo):

    '''Variáveis locais para receber a pontuação de cada time na ida'''
    pontuacao1_time1 = listas_jogo[0][2][0]
    pontuacao1_time2 = listas_jogo[0][2][1]
    
	'''Variáveis locais para receber a pontuação de cada time na volta'''    
    pontuacao2_time1 = listas_jogo[1][2][1]
    pontuacao2_time2 = listas_jogo[1][2][0]
    
    '''Variáveis locais para receber os nomes de cada time'''
    time1 = listas_jogo[0][0]
    time2 = listas_jogo[0][1]
    
    '''Variáveis locais para receber a pontuação total de cada time'''
    soma_time1 = 0
    soma_time2 = 0
    
    '''Condições para que cada time receba a pontuação correta na ida'''
    if pontuacao1_time1 == pontuacao1_time2:
        soma_time1 = 1
        soma_time2 = 1
    if pontuacao1_time1 > pontuacao1_time2:
        soma_time1 = 3
    if pontuacao1_time1 < pontuacao1_time2:
        soma_time2 = 3
    
    '''Condições para que cada time receba a pontuação correta na volta'''
    if pontuacao2_time1 == pontuacao2_time2:
        soma_time1 = soma_time1 + 1
        soma_time2 = soma_time2 + 1
    if pontuacao2_time1 > pontuacao2_time2:
        soma_time1 = soma_time1 + 3
    if pontuacao2_time1 < pontuacao2_time2:
        soma_time2 = soma_time2 + 3
    
    return {time2: soma_time2, time1: soma_time1}