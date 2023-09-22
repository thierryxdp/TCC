def faltas_por_time1(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:faltas_t1, nome_t2:faltas_t2}


def faltas_por_time2(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {jogoi[0]:faltas_t1, jogov[0]:faltas_t2}



def faltas_por_time3(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''
    
    return {jogoi[0]:jogoi[2][0] + jogov[2][1], jogov[0]:jogoi[2][1] + jogov[2][0]}


def faltas_por_time4(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1=jogoi[0][0]
    nome_t2=jogov[0][0]
    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:faltas_t1, nome_t2:faltas_t2}

def faltas_por_time5(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogoi[1]
    faltas_t1 = jogoi[2][0] + jogov[2][1]
    faltas_t2 = jogoi[2][1] + jogov[2][0]
    
    return {nome_t1:faltas_t1, nome_t2:faltas_t2}

def faltas_por_time6(jogoi, jogov):
    ''' retorna o numero total de faltas de cada time
    dadas duas listas dos jogos de ida  e volta
    list, list -> dict'''

    nome_t1=jogoi[0]
    nome_t2=jogov[0]
    faltas_t1 = jogoi[2][0] + jogoi[2][1]
    faltas_t2 = jogov[2][1] + jogov[2][0]
    
    return {nome_t1:faltas_t1, nome_t2:faltas_t2}


jogoCF=['Cormengo', 'Flamínthians',[10, 9]]
jogoFC=['Flamínthians', 'Cormengo', [5, 7]]