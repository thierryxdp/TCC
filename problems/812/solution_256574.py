def retira_pontuacao(frase):
    '''Dada uma fração qualquer retira suas pontuações, tais como travessão,
    vírgula, dois pontos, ponto, exclamação e interrogação. str -> str'''
    a = str.replace(frase,'-',' ')
    b = str.replace(a,',',' ')
    c = str.replace(b,':',' ')
    d = str.replace(c,';',' ')
    e = str.replace(d,'.',' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    return g