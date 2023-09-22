def retira_pontuacao(frase):
        
    frase = str(frase).replace('!',' ')
    frase = str(frase).replace('-',' ')
    frase = str(frase).replace('?',' ')
    frase = str(frase).replace('.',' ')
    frase = str(frase).replace(',',' ')
    frase = str(frase).replace(':',' ')
    frase = str(frase).replace(';',' ')
    return frase

def inverte(frase):
    frase = ""[::-1]
    return frase