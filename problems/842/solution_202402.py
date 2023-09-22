#Start your python function here
pontos_por_time(jogos):
    """Recebe lista de dois jogos onde dois times tem seus pontos 
    contabilizados e retorna um dicionario como 
    <nome do time> -> < total de pontos>;
    lista[2] --> dicionario[2]"""
    
    buffer_dic = {}
    
    #Time 1
    buffer_dic += {jogos[0][0] : jogos[0][2][0] + jogos[0][2][1],}
    #Time 1
    buffer_dic += {jogos[0][1] : jogos[0][2][1] + jogos[0][2][0]}
    
    return buffer_dic