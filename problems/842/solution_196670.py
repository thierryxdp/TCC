def pontos_por_time(partidas):
    '''recebe uma lista de dois elementos, onde cada um desses elementos  é tambem uma lista. A lista completa tem informac˜oes do numero de gols em dois jogos de futebol entre dois times.
    retorna um dicionario cujos mapeamentos sao: nome do time e numero de pontos na fase. dic->dic. '''
    p1 = partidas[0]
    p2 = partidas[1]
    pontuacao = {p1[0]:0,p1[1]:0}
    if p1[2][0] == p1[2][1]:
        pontuacao[p1[0]] = pontuacao[p1[0]] + 1
        pontuacao[p1[1]] = pontuacao[p1[1]] + 1
    elif p1[2][0]> p1[2][1]:
        pontuacao[p1[0]] = pontuacao[p1[0]] + 3
    else:
        pontuacao[p1[1]] = pontuacao[p1[1]] + 3
        
    if p2[2][0] == p2[2][1]:
        pontuacao[p2[0]] = pontuacao[p2[0]] + 1
        pontuacao[p2[1]] = pontuacao[p2[1]] + 1
    elif p2[2][0]> p2[2][1]:
        pontuacao[p2[0]] = pontuacao[p2[0]] + 3
    else:       
        pontuacao[p2[1]] = pontuacao[p2[1]] + 3
    
        
    return pontuacao