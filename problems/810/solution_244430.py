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
    frase=list.reverse(frase)
    ','.join(frase)
    return frase