def inverte(frase):
    def retira_pontuacao(frase):
        
    frase = str(frase).replace('!',' ')
    frase = str(frase).replace('-',' ')
    frase = str(frase).replace('?',' ')
    frase = str(frase).replace('.',' ')
    frase = str(frase).replace(',',' ')
    frase = str(frase).replace(':',' ')
    frase = str(frase).replace(';',' ')
    return frase

frase = "Inverter texto"[::-1]
return(frase)