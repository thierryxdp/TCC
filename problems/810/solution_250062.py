def inverte (frase):
    ''' retorna a ordem da frase invertida;tem como entrada 
    a frase; str->str'''
    frase1= str.replace(frase,'!',' ')
    frase2= str.replace(frase1,'?',' ')
    frase3= str.replace(frase2,'.',' ')
    frase4= str.replace(frase3,',',' ')
    frase5= str.replace(frase4,'-',' ')
    str.lower(frase5)
    return frase5