def retira_pontuacao(frase):
    'retira todos os caracteres de pontuacao de uma frase str->str'
    frase2 = str.replace(frase, '.', ' ')
    frase3 = str.replace(frase2, ',', ' ')
    frase4 = str.replace(frase3, '-', ' ')
    frase5 = str.replace(frase4, ':', ' ')
    return frase5