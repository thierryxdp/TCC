def retira_pontuacao(frase):
    "entra frase e retira a pontuação"
    return (frase.replace(',',' ').replace('.',' ').replace(';',' ').replace('?',' ').replace('!',' ').replace('-',' ').replace(':',' '))