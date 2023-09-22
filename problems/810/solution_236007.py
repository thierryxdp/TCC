def inverte(frase):
    a=frase.replace('.',' ')
    b=a.replace(',',' ')
    c=b.replace(':',' ')
    d=c.replace(';',' ')
    e=d.replace('!',' ')
    f=e.replace('?',' ')
    g=f.replace('-',' ')
    
    frase2=g.lower()
    frase3=str.split(frase2,' ')
    lista=frase3[::-1]
    lista2=lista[1:]
    
    return str.join('',lista2)