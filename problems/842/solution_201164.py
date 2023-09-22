def pontos_por_time(ls):
    """ função que calcula a quantidade de pontos
    de dois times em dois jogos de ida e volta , 
    onde a vitória credita 3 pontos , o empate 
    1 ponto e a derrota nenhum.
    assinatura: list --> dict
    testes:
    pontos_por_time([['a','b',[1,0]],['a','b',[2,2]]
    == {'a':4,'b':1}
    pontos_por_time([['a','b',[1,0]],['a','b',[2,2]]
    == {'a':4,'b':1}
    pontos_por_time([['a','b',[0,0]],['a','b',[4,2]]
    == {'a':4,'b':1}
    """
    ret = {'ida'[0]:0,'volta'[1]:0}
    ls[0]= 'ida'
    ls[1]= 'volta'
    t1= 'ida'[0]
    t2= 'ida'[1]
    
    
    gt1='ida'[2][0]
    gt2='ida'[2][1]
    
    contabiliza(ret,t1,t2,gt1,gt2)
    
    t1= 'volta'[0]
    t2= 'volta' [1]
    gt1='volta'[2][0]
    gt2='volta'[2][1]
    return ret
def contabiliza(ret,t1,t2,gt1,gt2):
    if gt1<gt2:
        ret[t2]+=3
        if gt1>gt2:
            ret[t2]+=3
            if gt1==gt2:
                ret[t2]+=1
                ret[t1]+=1