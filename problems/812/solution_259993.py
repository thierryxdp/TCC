def retira_pontuacao(frase):
    frasemsponto = frase.replace('!',' ').replace('?',' ').replace('...',' ').replace('—',' ').replace(';',' ').replace('.',' ').replace(':',' ')
    return frasemsponto