def retira_pontuacao(frase):
    caracteres = '-,:;.!?'
    for caracteres in caracteres:
        frase = frase.replace(caracteres, ' ')
    return frase