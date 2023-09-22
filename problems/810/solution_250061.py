def inverte (frase):
    ''' retorna a ordem da frase invertida;tem como entrada 
    a frase; str->str'''
    str.replace(frase,'!',' ')
    str.replace(frase,'?',' ')
    str.replace(frase,'.',' ')
    str.replace(frase,',',' ')
    str.replace(frase,'-',' ')
    str.lower(frase)
    return frase