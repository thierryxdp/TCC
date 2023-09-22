def retira_pontuacao ('z'):
    x = z
    a = str.replace (x,'.',' ')
    b = str.replace (a,',',' ')
    c = str.replace (b,'-',' ')
    d = str.replace (c,';',' ')
    e = str.replace (d,':',' ')
    f = str.replace (e,'?',' ')
    g = str.replace (f,'!',' ')
    return g