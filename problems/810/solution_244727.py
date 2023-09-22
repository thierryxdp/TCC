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
    return str.join(' ',list.reverse(palavras))