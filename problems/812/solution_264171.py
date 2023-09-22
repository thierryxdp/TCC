def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        x=frase[:]
        str.replace(x,k,' ')
        return x