def retira_pontuacao (frase) :
    """Funcao que dada uma frase retorna a frase onde todos os caracteres de pontuacao tenham sido substituidos por espaço"""
    frase = str.replace(frase, '-', " ")
    frase = str.replace(frase, ',', " ")
    frase = str.replace(frase, '.', " ")
    frase = str.replace(frase, ':', " ")
    frase = str.replace(frase, ';', " ")
    frase = str.replace(frase, '!', " ")
    frase = str.replace(frase, '?', " ")
    frase = str.replace(frase, '...', " ")
    frase = str.replace(frase, '#', " ")
    frase = str.replace(frase, '()', " ")
    frase = str.replace(frase, '[]', " ")
    frase = str.replace(frase, '"', " ")
    return frase