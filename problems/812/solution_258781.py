def retira_pontuacao(frase):
    index = 0
    for n in frase:
        if n == '!' or n == '?' or n == ':' or n == '.' or n == '-' or n == ';':
            frase.replace[n, ' ']
        index += 1
    return frase