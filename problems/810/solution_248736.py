def inverte(frase):
    """Função que dada uma frase, retira suas pontuações e inverte a ordem da frase"""
    """str->str"""
a=frase.replace('!',' ')
b=a.replace('?',' ')
c=b.replace('.',' ')
d=c.replace(',',' ')
e=d.replace(':',' ')
f=e.replace(';',' ')
g=f.split()
return g