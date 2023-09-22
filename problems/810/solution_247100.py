def inverte(texto):
    def retira_pontuacao(frase):
        
    frase = str(frase).replace('!',' ')
    frase = str(frase).replace('-',' ')
    frase = str(frase).replace('?',' ')
    frase = str(frase).replace('.',' ')
    frase = str(frase).replace(',',' ')
    frase = str(frase).replace(':',' ')
    frase = str(frase).replace(';',' ')
    return frase

texto = "Inverter texto"[::-1]
return(texto)