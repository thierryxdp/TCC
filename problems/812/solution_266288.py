def retira_pontuacao(frase):
    l = ['-',',','.',';',':','!','?']
    for x in l:
        frase = str.replace(frase,x,' ')
        return frase