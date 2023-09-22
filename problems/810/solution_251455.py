def inverte(frase):
    frase=str.lower(frase)
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.split(frase)
    frase1=list.reverse(frase)
    frase2=str.join(' ',frase1)
    return frase2