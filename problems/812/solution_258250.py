def retira_pontuacao(frase):
    """função que retorna a frase sem caracteres de pontuação.
    string --> string"""
    texto= str.replace(frase, '?', ' ')
    texto= str.replace(frase, '!', ' ')
    texto= str.replace(frase, '...', ' ')
    texto= str.replace(frase, '.', ' ')
    texto= str.replace(frase, '/', ' ')
    texto= str.replace(frase, ';', ' ')
    texto= str.replace(frase, ':', ' ')
    return frase