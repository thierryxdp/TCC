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
    palavras=str.split(frase)
    list.reverse(palavras)
    return str.join(' ',palavras)