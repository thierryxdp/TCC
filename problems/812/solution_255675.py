def retira_pontuacao(frase):
    '''dada uma frase, retorna substituindo todos os caracteres de pontuação por espaço;
    str --> str'''
    s=str.join(' ',str.split(frase,'...'))
    p=str.join(' ',str.split(s,'?'))
    d=str.join(' ',str.split(p,'!'))
    e=str.join(' ',str.split(d,'.'))
    f=str.join(' ',str.split(e,'-'))
    g=str.join(' ',str.split(f,','))
    h=str.join(' ',str.split(g,':'))
    i=str.join(' ',str.split(h,';'))
    return i