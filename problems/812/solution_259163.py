def retira_pontuacao(s):
    '''Retorna uma frase sem caracteres de pontuação.
    str -> str'''
    import string
    punct = string.punctuation
    for c in punct:
       s = s.replace(c, " ")
    return s