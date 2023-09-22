def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        return str.replace(frase,k,' ')