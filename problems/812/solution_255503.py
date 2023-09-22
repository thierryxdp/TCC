def retira_pontuacao(frase):
    s = frase
    saida = re.sub(r'[^\w\s]','',s)
    return saida