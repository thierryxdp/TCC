def retira_pontuacao(str):
    ''' str -> str'''
    texto = (str)
    x = '-' ',' ':' ';' '!' '?' '.'
    y = "                         "
    table = texto.maketrans(x,y);
    return (frase.translate(table))