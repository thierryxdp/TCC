def retira_pontuacao(frase):
    caracter=str('!')and str(',')and str('.')
    return str.replace(frase,caracter,' ')