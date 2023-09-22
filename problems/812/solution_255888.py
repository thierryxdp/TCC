def retira_pontuacao(frase):
    ''' funcao que retorne a frase sem caracteres de pontuacao'''
    '''str -> str'''
    x = "=,:;!?"
    y = "      "
    return frase.remove(x)