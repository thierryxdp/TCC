def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        x=frase.replace(k,' ')
    return x