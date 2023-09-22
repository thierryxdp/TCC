def retira_pontuacao (frase):
    s = str(frase)
    s = str.replace (s, ',', ' ')
    s = str.replace (s, '.', ' ')
    s = str.replace (s, '!', ' ')
    s = str.replace (s, '?', ' ')
    s = str.replace (s, ':', ' ')
    s = str.replace (s, ';', ' ')
    s = str.replace (s, '-', ' ')
    return s