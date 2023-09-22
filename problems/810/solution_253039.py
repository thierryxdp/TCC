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



def auxiliar(x):
    r = retira_pontuacao(x)
    s = r.lower()
    sp=s.split()
    sao = list.reverse(sp)
    return sao

def inverte(frase):
	lista = []
	lista = lista + (auxiliar(frase))
	
    return str.join(' ',lista)