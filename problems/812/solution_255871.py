def retira_pontuacao(frase):
    remocao1=str.split(frase,'-',',',':',';','!','?','.')
    remocao=str.join(' ',(remocao1))
    return remocao