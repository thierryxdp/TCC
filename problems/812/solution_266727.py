def retira_pontuacao(texto):
    a = str.replace(texto,',',' ')
    b = str.replace(a,':',' ') 
    c = str.replace(b,'—',' ') 
    d = str.replace(c,':',' ') 
    e = str.replace(d,';',' ') 
    f = str.replace(e,'!',' ') 
    g = str.replace(f,'?',' ')
    h = str.replace(g,'.',' ')
    return g