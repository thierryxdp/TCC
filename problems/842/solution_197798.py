def pontos_por_time(jogos):
    '''calcule uma função que receba uma lista de dois elementos, onde cada elemento é também uma lista, e retorne um dicionário com o nome do time e o número de pontos que o time fez na fase.list-->dict.'''
    nome_t1= jogos[0][0]
    nome_t2= jogos[0][1]
    if jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_t1:0, nome_t1:6}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        return {nome_t2:6, nome_t1:0}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_t1:3, nome_t2:3}
    elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        return {nome_t1:3, nome_t2:3}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]>jogos[1][2][0]:
        return {nome_t1:4, nome_t2:1}
    elif jogos[0][2][0]==jogos[0][2][1] and jogos[1][2][1]<jogos[1][2][0]:
        return {nome_t1:4, nome_t2:1}
    elif jogos[0][2][0]>jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        return {nome_t1:4, nome_t2:1}
    elif jogos[0][2][0]<jogos[0][2][1] and jogos[1][2][1]==jogos[1][2][0]:
        return {nome_t1:4, nome_t2:1}
    else:
        return {nome_t1:2, nome_t2:2}