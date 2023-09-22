def retira_pontuacao(frase):
    str1 = ''
    for v in frase:
        str1 += v
        if v == '-' or v == ',' or v == ':' or v == '.' or v == ';':
            str1 += ' '
    return str1