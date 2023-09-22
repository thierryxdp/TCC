def retira_pontuacao(frase):
    """ Função que retorna a frase dada como parâmetro, onde todos os caracteres de pontuação tenham sido substituídos por espaço;
        string -> string"""
    frase = str.replace(frase,'_',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,'.',' ')
    return frase