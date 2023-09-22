def retira_pontuacao(frase):
    res = re.sub(r'[^\w\s]', '', frase)
    return("+res)