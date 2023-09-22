def retira_pontuacao(texto):
    pontuacao = '!?,.`´'
    sempontos = ''
    for c in texto:
        if c.isalpha() or c == ' ':
            sempontos += c
    for palavra in texto:
        if palavra not in pontuacao:
            sempontos=sempontos+palavra
    return sempontos + ' '