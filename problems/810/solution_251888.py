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

def inverte(frase):
    return retira_pontuacao(frase.lower(frase[-1: :-1]))