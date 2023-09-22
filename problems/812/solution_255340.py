def retira_pontuacao(frase):
    ''' str -> str '''
    texto = str(frase)
    x = "-, : ; ! ?."
    y = "           "
    table = texto.maketrans(x,y);
    return (texto.translate(table))