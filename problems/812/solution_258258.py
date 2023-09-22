def retira_pontuacao(frase):
    """função que retorna a frase sem caracteres de pontuação.
    string --> string"""
    frase=str.replace(frase, '?', ' ')
    frase=str.replace(frase, '!', ' ')
    frase=str.replace(frase, '...', ' ')
    frase=str.replace(frase, '.', ' ')
    frase=str.replace(frase, '/', ' ')
    frase=str.replace(frase, ';', ' ')
    frase=str.replace(frase, ':', ' ')
    frase=str.replace(frase, ',', ' ')
    frase=str.replace(frase, '-', ' ')
    return frase