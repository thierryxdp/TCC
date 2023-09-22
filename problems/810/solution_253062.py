def retira_pontuacao(frase):
    b=frase.replace('!',' ')
    b=b.replace('.',' ')
    b=b.replace('?',' ')
    b=b.replace(';',' ')
    b=b.replace(':',' ')
    b=b.replace(',',' ')
    b=b.replace('-',' ')
    b=b.replace('...',' ')
    
def inverte(frase):
    c=retira_pontuacao(frase)
    c=c.lower
    l=c.split()
    l=list.reverse(l)
    d=str.join(' ',l)
    return d