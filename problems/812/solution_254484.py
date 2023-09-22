def retira_pontuacao(frase):
    subs = ('-',',',':',';','.','!','?','...')
    return frase.split(subs," ")