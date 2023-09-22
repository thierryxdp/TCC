def retira_pontuacao(frase):
    '''Dada uma frase, retorna outra frase onde todos os caracteres de pontuação tenham sido substituidos 
    por espaço. str-> str''' 
    f = frase
    f= str.replace(frase,'-',' ')
    f= str.replace(frase,',',' ')
    f= str.replace(frase,':',' ')
    f= str.replace(frase,';',' ')
    f= str.replace(frase,'.',' ')
    f= str.replace(frase,'?',' ')
    f= str.replace(frase,'!',' ')
    f= str.replace(frase,'...',' ')
    return f