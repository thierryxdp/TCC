def inverte(frase):
    a=frase.replace('-','.')
    b=a.replace(',','.')
    c=b.replace(':','.')
    d=c.replace(';','.')
    e=d.replace('!','.')
    f=e.replace('?','.')
    frase2=f.lower()
    lista=frase2.split('.')
    lista=lista[::-1]
    
    return ''.join(lista)