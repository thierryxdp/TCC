#Start your python function here
def empate(jogo_1, jogo_2):
    """Verifica se houve empate"""
def pontos_por_time(jogos):
    """Recebe lista de dois jogos onde dois times tem seus pontos 
    contabilizados e retorna um dicionario como 
    <nome do time> -> < total de pontos>;
    lista[2] --> dicionario[2]"""
    
    time_1 = jogos[0][0]
    time_2 = jogos[0][1]
    buffer_dict = {time_1: 0, time_2: 0}
    
    jogo_1 = jogos[0][2]
    jogo_2 = jogos[1][2]
    
    if (jogo_1[0] == jogo_1[1]):
        # Empate primeiro jogo
    	buffer_dict[time_1] += 1
    	buffer_dict[time_2] += 1
    elif (jogo_1[0] > jogo_1[1]):
        # Caso time_1 tenha vencido jogo 1
        buffer_dict[time_1] += 3
    elif (jogo_1[0] < jogo_1[1]):
        # Caso time_2 tenha vencido jogo 1
        buffer_dict[time_2] +=3
        
    if (jogo_2[0] == jogo_2[1]):
        # Empate segundo jogo
        buffer_dict[time_1] += 1
    	buffer_dict[time_2] += 1
    elif (jogo_2[1] > jogo_2[0]):
        # Caso time_1 tenha vencido jogo 2
        buffer_dict[time_1] += 3
    elif (jogo_2[1] < jogo_2[0]):
        # Caso time_2 tenha vencido jogo 2
        buffer_dict[time_2] +=3
    
    return buffer_dict