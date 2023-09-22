def retira_pontuacao(frase):
    s=str.join(' ',str.split(frase,'...'))
    p=str.join(' ',str.split(s,'?'))
    d=str.join(' ',str.split(p,'!'))
    e=str.join(' ',str.split(d,'.'))
    f=str.join(' ',str.split(e,'-'))
    g=str.join(' ',str.split(f,','))
    h=str.join(' ',str.split(g,':'))
    i=str.join(' ',str.split(h,';'))
    return i

def inverte(frase):
    '''dada uma frase, retorna em ordem invertida;
    str --> str'''
    f1=retira_pontuacao(frase)
    f2=str.split(f1)
    f3=str.join(' ',f2[::-1])
    return str.lower(f3)