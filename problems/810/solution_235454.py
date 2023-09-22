def inverte(frase):
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.split(frase)
    frase=frase[-1::-1]
    frase=str.join(' ',frase)
    return str.lower(frase)