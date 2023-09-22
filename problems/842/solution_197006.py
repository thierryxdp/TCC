def pontos_por_time (fase):
    '''dada uma lista com 2 elementos(onde cada elemento tambem é uma lista) com informações do placar em dois jogos de
       futebol entre dois times, retorna um dicionario indicando o numero total de pontos de cada time.
       : list -> dict
    '''
    ida = fase[0]
    volta = fase[1]
    
    ida[0] = volta[1]
    ida[1] = volta[0]
    
    placar1 = ida[2]
    placar2 = volta[2]
    
    v = 3
    e = 1
    d = 0
    
    pontos = {}
    if ida[2][0]>ida[2][1]:
        pontos = pontos[ida[0]] = v
        pontos = pontos[ida[1]] = d
    if ida[2][0]<ida[2][1]:
        pontos = pontos[ida[1]] = v 
        pontos = pontos[ida[0]] = d
    if ida[2][0] == ida[2][1]:
        pontos = pontos[ida[0]] = e
        pontos = pontos[ida[1]] = e
        return pontos