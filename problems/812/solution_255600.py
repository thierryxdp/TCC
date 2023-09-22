def retira_pontuacao(frase):
    ''' funcao que retorne a frase sem caracteres de pontuacao'''
    '''str -> str'''
    x = "-.:;!?,"
    y = "       "
    table = frase.maketrans(x,y)
    return (frase.translate(table))