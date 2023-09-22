#
#
#
#
def inverte(frase):
    
    frase=str.lower(frase)
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.split(frase)
    list.reverse(frase)
    str(list)
    return frase