def retira_pontuacao(frase): 
    x = re.sub('[?!,.-]', ' ', frase)
    return x