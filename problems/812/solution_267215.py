def retira_pontuacao(texto):
    pontuacao = '!?,-.`´'
    sempontos = ''
    for palavra in texto:
        if palavra not in pontuacao:
            sempontos= sempontos + palavra
    return sempontos + ''