def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        x=str.replace(frase,k,' ')
    return x