def retira_pontuacao(x):
    frase=x
    frase = frase.replace('.',' ') and frase.replace(',',' ') and frase.replace(':',' ') and 
    frase.replace(';',' ') and frase.replace('—',' ')
    
    return frase