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

def min(x):
    return pev.lower()

def invertendo_lista(x):
    r=[]
    r.append(x)
    return r.reverse()

def inverte(frase):
    return str.join(' ',invertendo_lista(frase))