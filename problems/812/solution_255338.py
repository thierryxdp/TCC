def retira_pontuacao(frase):
    texto = str(frase)
    x = "-, : ; ! ?."
    y = "           "
    table = texto.maketrans(x,y);
    return texto.translate(table)