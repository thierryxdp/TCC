def retira_pontuacao(frase):
    if ("!",".",",","?","-",":",";") in frase:
        frase = frase.sub("[!.,:;?/-]", ' ', frase)
        return frase