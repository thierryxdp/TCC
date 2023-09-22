def inverte(frase):
    
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.lower(frase)
    return str.join(list.reverse(str.split(frase)),' ')