def inverte(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase=f.split('.')
    
    return str.join('',frase[::-1)