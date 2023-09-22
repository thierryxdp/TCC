def retira_pontuacao(frase):
    ''' str -> str'''
    texto = (frase)
    x = '-' ',' ':' ';' '!' '?' '.'
    y = "                         "
    table = texto.maketrans(x,y);
    return (frase.translate(table))