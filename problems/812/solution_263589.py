def retira_pontuacao(frase):
    for k in ['.','...',',',';','-','!','?',':']:
        str.strip(frase,k)
        return frase