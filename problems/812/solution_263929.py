def retira_pontuacao(frase):
    
    frase.replace('...',' ',-1)
    frase.replace('.',' ',-1)
    frase.replace('-',' ',-1)
    frase.replace(',',' ',-1)
    frase.replace(':',' ',-1)
    frase.replace(';',' ',-1)
    frase.replace('?',' ',-1)
    frase.replace('!',' ',-1)
    
    return frase