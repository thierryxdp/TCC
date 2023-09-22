def retira_pontuacao(frase):
    x=frase[:]
    for k in ['.','...',',',';','-','!','?',':']:
        str.replace(x,k,' ')
    return x