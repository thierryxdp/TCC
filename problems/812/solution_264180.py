def retira_pontuacao(frase):
    for k in ['.','...','?','!',':','-',',',';']:
        if k in frase:
            x=str.replace(frase,k,' ')
            y=str.replace(x,x[-1],' ')
    return y