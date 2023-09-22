def inverte (frase):
    frase= str.lower(frase)
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.split(frase,' ')
    frase= frase[::-1]
    frasefinal= str.join(' ',frase)
    return frasefinal