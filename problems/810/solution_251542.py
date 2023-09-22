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
    i=[]
    for x in frase:
        i+=x
    return i