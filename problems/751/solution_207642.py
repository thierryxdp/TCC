def frase(frase):
    ''' função que transforma caracteres em espaco
   (frase) = str
   saida = str'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    return frase