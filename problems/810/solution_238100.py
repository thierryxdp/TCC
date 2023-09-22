def retira_pontuacao(frase):
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
def inverte(frase):
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    frase=frase[::-1]
    
    return frase