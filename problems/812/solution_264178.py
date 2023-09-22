def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        if k in frase:
            str.replace(frase,k,' ')
    return frase