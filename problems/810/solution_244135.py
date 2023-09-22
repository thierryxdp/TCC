#
#
#
def inverte(frase):
    str.replace(frase,'.',' ')#remove pontuação
    str.replace(frase,',',' ')#remove pontuação
    str.replace(frase,'?',' ')#remove pontuação
    str.replace(frase,'!',' ')#remove pontuação
    str.replace(frase,':',' ')#remove pontuação
    str.replace(frase,';',' ')#remove pontuação
    str.replace(frase,'-',' ')#remove pontuação
    str.lower(frase)#abaixa a frase
   
    return frase