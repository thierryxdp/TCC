def inverte(frase):
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    b=str.split(frase)
    a=b[::-1]
    c=str.join(' ',a)
    return str.lower(c)