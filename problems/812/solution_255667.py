def retira_pontuacao(frase):
    frase=frase.replace('_','.').replace(',','.').replace(':','.').replace(';','.')
    frase=frase.split('.')
    return str.join(' ',frase)