def retira_pontuacao(frase):
    f1 = string.replace(frase, ',', ' ', 10)
    f2 = string.replace(f1, '-', ' ', 10)
    f3 = string.replace(f2, ';', ' ', 10)
    f4 = string.replace(f3, ':', ' ', 10)
    f5 = string.replace(f4, '!', ' ', 10)
    f6 = string.replace(f5, '?', ' ', 10)
    f7 = string.replace(f6, '.', ' ', 10)
    f8 = string.replace(f7, '/', ' ', 10)
    return f8