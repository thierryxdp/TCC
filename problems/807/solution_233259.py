def retira_pontuacao(texto):
    pontuação = '!?,-.'
    sempontos = ''
    for palavra in texto:
        if palavra not in pontuação:
            sempontos= sempontos + palavra
    return sempontos