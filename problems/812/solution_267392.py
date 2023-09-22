def retira_pontuacao(frase):
    caracteres = ',', '.'
    if caracteres in frase:
        a = frase.replace(caracteres, ' ')
        return a