def retira_pontuacao(frase):
    a = str.split(frase, ',')
    c = len(a)
    b = str.replace(frase,',','',c)
    return b