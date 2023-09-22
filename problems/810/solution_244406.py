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
    return frase