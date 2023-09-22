def retira_pontuacao(frase):
    'retira todos os caracteres de pontuacao de uma frase str->str'
    frase2 = str.replace(frase, '.', ' ')
    frase3 = str.replace(frase2, ',', ' ')
    frase4 = str.replace(frase3, '-', ' ')
    frase5 = str.replace(frase4, ':', ' ')
    frase6 = str.replace(frase5, '!', ' ')
    frase7 = str.replace(frase6, '?', ' ')
    return frase7
def inverte(frase):
    'inverte a frase dada str->str'
    frase1 = retira_pontuacao(frase)
    frase2 = str.split(frase1)
    frase3 = reversed(frase2)
    frase4 = list (frase3)
    frase5 = str.join(frase4, ' ')
    return frase5