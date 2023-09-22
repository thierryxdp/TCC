def retira_pontuacao(frase):
    '''Dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
       :param frase: str
       :return: str'''
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    return frase