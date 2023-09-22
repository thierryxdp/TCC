def inverte(frase):
    """função que retorne uama outra frase que contenha as mesmas palavras da frase da entrada na ordem inversa e que não possui letras maiúsculas e nem pontuação; str-> str"""
    frase2=str.lower(frase)
    a=frase2.replace('...','.')
    b=a.replace('...','.')
    c=b.replace('!','.')
    d=c.replace('?','.')
    e=d.replace('-','.')
    f=e.replace(',','.')
    g=f.replace(':','.')
    h=g.replace(';','.')
    i=h.replace('.','')
    frase2=str.split(i)
    frase2=frase2[::-1]
    frase2=str.join('',frase2)
    return frase2