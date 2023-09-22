def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase
    onde todos os caracteres de pontuação(travessão, vírgula,
    dois pontos, ponto e vírgula, além da pontuação de encerramento
    de frase) tenham sido substituídos por espaço.
    str -> str"""
    frase1 = str.replace(frase, '!', ' ')
    frase2 = str.replace(frase1, '?', ' ')
    frase3 = str.replace(frase2, ';', ' ')
    frase4 = str.replace(frase3, '...', ' ')
    frase5 = str.replace(frase4, ',', ' ')
    frase6 = str.replace(frase5, ':', ' ')
    frase7 = str.replace(frase6, '.', ' ')
    frase8 = str.replace(frase7, '-', ' ')
    return frase8

def inverte(frase):
    """Função que, dada uma frase, retorna uma outra frase
    que contenha as mesmas palavras da frase de entrada na
    ordem inversa, sem letras maiúsculas, e sem a pontuação.
    str -> str"""
    retira_pontuacao(frase)
    frase9 = str.lower(retira_pontuacao(frase))
    lista = str.split(frase9)
    list.reverse(lista)
    return str.join(" ",lista)