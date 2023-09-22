def retira_pontuacao(frase):
    frase1 = str.replace(frase,',',' ',2)
    if ',' in frase:
        return frase1