def retira_pontuacao(string):
    f1 = string.replace(string, ',', ' ')
    f2 = string.replace(f1, '-', ' ')
    f3 = string.replace(f2, ';', ' ')
    f4 = string.replace(f3, ':', ' ')
    f5 = string.replace(f4, '!', ' ')
    f6 = string.replace(f5, '?', ' ')
    f7 = string.replace(f6, '.', ' ')
    f8 = string.replace(f7, '/', ' ')
    return f8