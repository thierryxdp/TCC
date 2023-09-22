def pontos_por_time (fase):
    '''dada uma lista com 2 elementos(onde cada elemento tambem é uma lista) com informações do placar em dois jogos de
       futebol entre dois times, retorna um dicionario indicando o numero total de pontos de cada time.
       : list -> dict
    '''
    fase[0] = ida
    fase[1] = volta
    
    ida[0] = volta[1]
    ida[1] = volta[0]
    
    ida[2] = placar1
    volta[2] = placar2
    
    pontos = {}
    if ida[2][0]>ida[2][1]:
        pontos[ida[0]] = 3 and pontos[ida[1]] = 0
    if ida[2][0]<ida[2][1]:
        pontos[ida[1]] = 3 and pontos[ida[0]] = 0
    if ida[2][0] == ida[2][1]:
        pontos[ida[0]] = 0 and pontos[ida[1]] = 0