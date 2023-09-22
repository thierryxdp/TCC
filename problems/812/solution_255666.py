def retira_pontuacao(frase):
    frases=frases.replace('_','.').replace(',','.').replace(':','.').replace(';','.')
    frases=frases.split('.')
    return str.join(' ',frases)