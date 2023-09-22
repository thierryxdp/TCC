def retira_pontiacao(frase):
    ''' 
    dada uma frase retira toda as pontuações desta 
    frase e retorna a frase sem as pontuações
    '''
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    return frase