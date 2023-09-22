def retira_pontuacao (frase):
    """ dada uma frase, retorne a frase onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço.
    
    entrada ->str
    retorna ->str
    """
    
    frase2=str.replace (frase,'-',' ')
    frase2=str.replace (frase2,',',' ')
    frase2=str.replace (frase2,':',' ')
    frase2=str.replace (frase2,';',' ')
    frase2=str.replace (frase2,'.',' ')
    frase2=str.replace (frase2,'?',' ')
    frase2=str.replace (frase2,'!',' ')
    return frase2