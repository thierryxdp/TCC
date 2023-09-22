def inverte(texto):
    texto=str.replace(texto,',',' ')
    texto=str.replace(texto,'.',' ')
    texto=str.replace(texto,'-',' ')
    texto=str.replace(texto,':',' ')
    texto=str.replace(texto,';',' ')
    texto=str.replace(texto,'?',' ')
    texto=str.replace(texto,'!',' ')
    texto=str.replace(texto,'...',' ')
    x=str.split(texto)
    z=x[::-1]
    y=str.join(' ',z)
    return str.lower(y)