def retira_pontuacao(frase):
    x=frase[:]
    for k in ['.','...',',',';','-','!','?',':']:
        if k in x:
            str.replace(x,k,' ')
    return x