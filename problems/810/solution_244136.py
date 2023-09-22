#
#
#
def inverte(frase):
    str.lower(frase)#abaixa a frase
    str.replace(frase,'.',' ')#remove pontuação
    str.replace(frase,',',' ')#remove pontuação
    str.replace(frase,'?',' ')#remove pontuação
    str.replace(frase,'!',' ')#remove pontuação
    str.replace(frase,':',' ')#remove pontuação
    str.replace(frase,';',' ')#remove pontuação
    str.replace(frase,'-',' ')#remove pontuação      
    return frase