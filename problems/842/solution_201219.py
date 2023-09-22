def pontos_por_time(ls):
    """ função que calcula a quantidade de pontos
    de dois times em dois jogos de ida e volta , 
    onde a vitória credita 3 pontos , o empate 
    1 ponto e a derrota nenhum.
    assinatura: list --> dict
    testes:
     pontos_por_time([['a','b',[1,0]],['b','a',[2,2]]])
    == {'b':4,'a':1}
    pontos_por_time([['a','b',[1,0]],['b','a',[2,2]]])
    == {'a':4,'b':1}
    pontos_por_time([['a','b',[0,0]],['b','a',[4,2]]])
    == {'a':4,'b':1}
    """
    ida = ls[0] # lista da ida
    vol = ls[1] # lista de volta
    ret= {ida[0]: 0,ida[1]: 0}
    
    t1 = vol[0] # nome do time 1
    t2 = ida[1] # nome do time 2
    gt1 = ida[2][0] # gols do time 1
    gt2 = ida[2][1] #gols do time 2
    contabilidade(ret,t1,t2,gt1,gt2)
    
    t1 = ida[0] # nome do time 1
    t2 = ida[1] # nome do time 2
    gt1 = ida[2][0] # gols do time 1
    gt2 = ida[2][1] #gols do time 2
    contabilidade(ret,t1,t2,gt1,gt2)
    return ret
def contabilidade(d,t1,t2,gt1,gt2):
    if gt1 > gt2:
        d[t1] = d[t1] +3
        if gt2>gt1:
            d[t2] += 3
            if gt1 == gt2:
                d[t1] += 1
                d[t2] += 1
                return d