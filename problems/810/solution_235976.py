def inverte(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase2=f.split('.')
    frase2=frase2[::-1]
    
    return str.join('',frase2)