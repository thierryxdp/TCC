def inverte(frase):
    """Função que dada uma frase, retira suas pontuações e inverte a ordem da frase"""
    """str->str"""
    a=frase.replace('!',' ')
    b=a.replace('?',' ')
    c=b.replace('.',' ')
    d=c.replace(',',' ')
    e=d.replace(':',' ')
    f=e.replace(';',' ')
    g=f.replace('-',' ')
    h=g.split()
    i=h[::-1]
    k=' '.join(i)
    j=str.lower(k)
    
    return j