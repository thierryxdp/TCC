def retira_pontuacao(frase):
    frase1 = str.replace(frase,str.strip(frase,',.!-?:'),2)
    return frase1