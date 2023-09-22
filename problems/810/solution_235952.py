def inverte(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase=f.split('.')
    frase2=frase.join('',frase)
    return frase2[::-1]