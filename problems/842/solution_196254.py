def pontos_por_time(jogo1:list,jogo2:list)->dict:
    """recebe uma lista de dois elementos onde cada elemento também é uma lista, retornando o nome do time e o numero total de pontos na fase"""
    nome_t1= jogo1[0]
    nome_t2= jogo2[0]
    if int(jogo1[2][0])>int(jogo1[2][1]):
        pontos_t1 = 3
        pontos_t2 = 0
    elif int(jogo1[2][0])<int(jogo1[2][1]):
        pontos_t1 = 0
        pontos_t2 = 3
    elif int(jogo1[2][0])== int(jogo1[2][1]):
        pontos_t1 = 1
        pontos_t2 = 1
    if int(jogo2[2][0])>int(jogo2[2][1]):
        pontos_t1 = pontos_t1 + 0
        pontos_t2 = pontos_t2 + 3
    elif int(jogo2[2][0])<int(jogo2[2][1]):
        pontos_t1 = pontos_t1 + 3
        pontos_t2 = pontos_t2 + 0
    elif int(jogo2[2][0])== int(jogo2[2][1]):
        pontos_t1 = pontos_t1 + 1
        pontos_t2 = pontos_t2 + 1
    return {nome_t1:int(pontos_t1), nome_t2:int(pontos_t2)}