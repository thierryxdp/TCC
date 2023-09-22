def inverte(frase):
    '''dada uma frase, retorna a mesma sem letras maiusculas, sem pontuação e ao contrário
str-->str'''
    frase1=str.replace(frase,'-',' ')
    frase2=str.replace(frase1,',',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,';',' ')
    frase5=str.replace(frase4,'.',' ')
    frase6=str.replace(frase5,'!',' ')
    frase_final1=str.replace(frase6,'?',' ')
    frase_minuscula=str.lower(frase_final1)
    frase_separada=str.split(frase_minuscula)
    return frase_separada