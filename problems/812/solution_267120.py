def retira_pontuacao(x):
    frase=x
    frase.replace('.',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('—',' ')
    return frase