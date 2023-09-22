def retira_pontuacao(texto):
    '''Recebe um texto e retorna ele com espaço no lugar da pontuação; str -> str'''
    a = str.join(' ',str.split(texto,'...'))
    b = str.join(' ',str.split(a,'-'))
    c = str.join(' ',str.split(b,';'))
    d = str.join(' ',str.split(c,':'))
    e = str.join(' ',str.split(d,'!'))
    f = str.join(' ',str.split(e,'?'))
    g = str.join(' ',str.split(f,','))
    h = str.join(' ',str.split(g,'.'))
    return h