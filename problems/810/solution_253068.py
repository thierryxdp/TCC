def retira_pontuacao(frase):
    b=frase.replace('!',' ')
    b=b.replace('.',' ')
    b=b.replace('?',' ')
    b=b.replace(';',' ')
    b=b.replace(':',' ')
    b=b.replace(',',' ')
    b=b.replace('-',' ')
    b=b.replace('...',' ')
    return b
    
def inverte(frase):
    c=retira_pontuacao(frase)
    c=c.lower()
    l=c.split()
    l=l.reverse()
    return l