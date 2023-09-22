def retira_pontuacao(x):
    frase=x
    frase = frase.replace('.',' ') = frase.replace(',',' ')
    = frase.replace(':',' ')
    = frase.replace(';',' ') 
    = frase.replace('—',' ')
    
    return frase