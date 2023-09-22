def retira_pontuacao(frase):
    f=frase
        f=frase.replace(',',' ')
        f=frase.replace('.',' ')
        f=frase.replace('-',' ')
        f=frase.replace(':',' ')
        f=frase.replace(';',' ')
    return f