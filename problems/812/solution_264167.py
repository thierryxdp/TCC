def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        str.replace(frase,k,' ')