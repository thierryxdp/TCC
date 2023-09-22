def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        if k in frase:
            x=str.split(frase,k)
        return x