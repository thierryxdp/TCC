def retira_pontuacao(frase):
    """função que retorne a frase onde todos os caracteres de pontuação tenha sido substituídos por espaço; str -> str"""
    a=frase.replace('...','.')
    b=a.replace('...','.')
    c=b.replace('!','.')
    d=c.replace('?','.')
    e=d.replace('-','.')
    f=e.replace(',','.')
    g=f.replace(':','.')
    h=g.replace(';','.')
    return h.replace('.',' ')