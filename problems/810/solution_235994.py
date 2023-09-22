def inverte(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase2=f.lower()
    frase3=str.split(frase2,'.')
    lista=frase3[::-1]
    
    return str.join(' ',lista)