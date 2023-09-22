def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        if k in frase:
            x=str.replace(frase,k,' ')
    return x