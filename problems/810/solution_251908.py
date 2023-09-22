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
    frase.lower()
    return retira_pontuacao(frase[-len(frase):-1])