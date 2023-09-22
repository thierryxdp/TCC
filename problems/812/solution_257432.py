def retira_pontuacao (frase):
    s = str(frase)
    str.replace (s, ',', ' ')
    str.replace (s, '.', ' ')
    str.replace (s, '!', ' ')
    str.replace (s, '?', ' ')
    str.replace (s, ':', ' ')
    str.replace (s, ';', ' ')
    str.replace (s, '-', ' ')