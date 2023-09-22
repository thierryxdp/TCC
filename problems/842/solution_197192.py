def pontos_por_time(jogo1,jogo2):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar; 
    list, list -> dict"""
    nome1 = jogo1[0]
    nome2 = jogo2[0]
    gols1 = jogo1[2][0] + jogo2[2][1]
    gols2 = jogo1[2][1] + jogo2[2][0]
    return nome1