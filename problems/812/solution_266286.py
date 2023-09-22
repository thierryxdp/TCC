def retira_pontuacao(frase):
    l = ['-',',','.',';',':','!','?']
    for x in l:
        codigo = str.replace(frase,str(x),' ')
        return codigo