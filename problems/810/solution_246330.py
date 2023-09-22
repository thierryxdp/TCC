#a função inverte a frase
#str->str
def inverte(frase):
    a=frase.replace(',',' ')
    b=a.replace('-',' ')
    c=b.replace(':',' ')
    d=c.replace(';',' ')
    e=d.replace('?',' ')
    f=e.replace('!',' ')
    g=f.replace('.',' ')
    h=g.lower()
    i=h.split()
	i.reverse()
    str(i)
    return(i)