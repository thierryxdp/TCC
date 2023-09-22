def retira_pontuacao(frase):
    frase1 = str.replace(frase,',',' ',2)
    if ',' and '.' in frase:
        return str.strip(frase1,',.')