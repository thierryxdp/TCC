def retira_pontuacao(frase):
    l = '-',',','.',';',':','!','?'
    for x in l:
        str.replace(frase,l,' ')
        return frase