def retira_pontuacao(x):
    ponto=x.replace('.',' ')
    exc=ponto.replace('!', ' ')
    inte=exc.replace('?',' ')
    ret=inte.replace('...', ' ')
    vir=ret.replace(',',' ')
    trav=vir.replace('-',' ')
    dp=trav.replace(':',' ')
    pev=dp.replace(';',' ')
    
    
    return pev

def invertendo(x):
    r = []
    r = r+x
    r.reverse()
    return r

def inverte(x):
    retira_pontuacao(x)
    invertendo(x)
    
    return x