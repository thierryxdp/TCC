#
#
#
def inverte(frase):   
    str.replace(frase,'.',' ')
    str.replace(frase,',',' ')
    str.replace(frase,'?',' ')
    str.replace(frase,'!',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'-',' ')
    return frase