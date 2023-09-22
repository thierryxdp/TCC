def retira_pontuação(frase):
    '''função que dada uma frase, retorne a frase onde todos os caracteres de pontuação são substituídos por um espaço.
    str ->str'''
    
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    
    return frase