def retira_pontuacao(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase_2=f.replace('.',' ')
    return frase_2