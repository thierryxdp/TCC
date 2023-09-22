def pontos_por_time(jogoi,jogov):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar; 
    list, list -> dict"""
    nome1 = jogoi[0]
    nome2 = jogov[0]
    gols1 = jogoi[2][0] + jogov[2][1]
    gols2 = jogoi[2][1] + jogov[2][0]
    return nome2