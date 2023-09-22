def retira_pontuacao(frase):
    
    a=frase.replace('...',' ',-1)
    b=a.replace('.',' ',-1)
    c=b.replace('-',' ',-1)
    d=c.replace(',',' ',-1)
    e=d.replace(':',' ',-1)
    f=e.replace(';',' ',-1)
    g=f.replace('?',' ',-1)
    h=g.replace('!',' ',-1)
    
    return frase