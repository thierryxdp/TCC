def cormengo1 (jogos):
    '''retorna o resultado 1 do cormengo
    list->int'''
    if 'Cormengo' == (jogos[:1])[:1]:
        return (jogos[:1]) [2:3])[:1]
    else:
        return ((jogos[:1])[2:3])[1:2]
        
def flaminthians1 (jogos):
    '''retorna o resultado 1 do flaminthians
    list->int'''
    if 'Flamínthians' == (jogos[:1])[:1]:
        return (jogos[:1]) [2:3])[:1]
    else:
        return ((jogos[:1])[2:3])[1:2]
    
def cormengo2 (jogos):
    '''retorna o resultado 2 do cormengo
    list->int'''
    if 'Cormengo' == (jogos[1:2])[:1]:
        return (jogos[1:2]) [2:3])[:1]
    else:
        return ((jogos[1:2])[2:3])[1:2]

def flaminthians2 (jogos):
    '''retorna o resultado 2 do flaminthians
    list->int'''
    if 'Flamínthians' == (jogos[1:2])[:1]:
        return (jogos[1:2]) [2:3])[:1]
    else:
        return ((jogos[1:2])[2:3])[1:2] 
    
def cormengo_pt1 (cormengo1,flaminthians1):
    '''retorna o ponto ganho do cormengo
    int->int'''
    if cormengo1 > flaminthians1:
        return 3
    elif cormengo1 == flaminthians1:
        return 1
    else:
        return 0

def flaminthians_pt1 (cormengo1,flaminthians1):
    '''retorna o ponto ganho do flaminthians
    int -> int'''
    if flaminthians1 > cormengo1:
        return 3
    elif flaminthians1 == cormengo1:
        return 1
    else:
        return 0

def cormengo_pt2 (cormengo2,flaminthians2):
    '''retorna o ponto ganho do cormengo
    int->int'''
    if cormengo2 > flaminthians2:
        return 3
    elif cormengo2 == flaminthians2:
        return 1
    else:
        return 0
    
def flaminthians_pt2 (cormengo2,flaminthians2):
    '''retorna o ponto ganho do flaminthians
    int -> int'''
    if flaminthians2 > cormengo2:
        return 3
    elif flaminthians2 == cormengo2:
        return 1
    else:
        return 0
    
def pontos_por_time (jogos):
    '''recebe uma lista com os nomes dos times, Cormengo e Flamínthians,
    e uma outra lista contida nessa contendo o valor do placar e devolve
    um dicionário contendo o nome dos times e seus pontos obtidos por partida
    list->dicionario'''
    
    Tabela_pontos{'Cormengo':cormengo_pt1+cormengo_pt2, 'Flamínthians':flaminthians_pt1+flaminthians_pt2}
    
    return Tabela_pontos