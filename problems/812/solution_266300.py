def retira_pontuacao(frase):
    l = [',',':',';','.','!','?']
    return (str.replace(frase,l,' '))