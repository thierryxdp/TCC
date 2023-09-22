def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        x=str.split(frase,k)
        return x