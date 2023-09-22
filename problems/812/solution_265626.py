def retira_pontuacao(frase):
    frase = frase.sub("[!.,:;?/-]", ' ', frase)
    return frase