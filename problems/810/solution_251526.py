def inverte(frase):
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    frase=frase[::-1]
    frase=frase[0]+' '+frase[1]
    return frase