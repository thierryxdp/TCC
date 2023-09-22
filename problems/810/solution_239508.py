def retira_pontuacao(frase):
    """ A retira todas as pontuações de uma frase e retorna a mesma sem tais pontuações"""
    frase1=frase.replace( '?',' ')
    frase2=frase1.replace('!',' ')
    frase3=frase2.replace('.',' ')
    frase4=frase3.replace(';',' ')
    frase5=frase4.replace(',',' ')
    frase6=frase5.replace(':',' ')
    frase7=frase6.replace('-',' ')
    return frase7
def inverte(frase):
    frase= str.lower(frase)
    frase= retira_pontuacao(frase)
    frase1= frase.split(frase,' ')
    resp= str.join(' ', frase1)
    resp= def inverte(frase):
    frase= str.lower(frase)
    frase=retira_pontuacao(frase)
    frase1= str.split(frase,' ')
    resp= str.join(' ', frase1)
    def inverte(frase):
    frase= str.lower(frase)
    frase=retira_pontuacao(frase)
    frase1= str.split(frase,' ')
    final= frase1.reverse()
    resp= str.join(' ', final)
    
    return resp