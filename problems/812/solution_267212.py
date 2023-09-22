def retira_pontuacao(texto):
    sempontos = ''
    for c in texto:
        if c.isalpha() or c == ' ':
            sempontos += c
    return sempontos + ' '