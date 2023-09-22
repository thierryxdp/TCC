def retira_pontuacao(frase):
    '''Dada uma frase, retorna outra frase onde todos os caracteres de pontuação tenham sido substituidos 
    por espaço. str-> str''' 
    frase= str.replace(frase,'-',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.replace(frase,'...',' ')
    return frase