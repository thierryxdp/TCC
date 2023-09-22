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
    frase=frase[0]+' '+frase[1]+' '+frase[2]+' '+frase[3]+' '+frase[4]+' '+frase[5]
    return frase