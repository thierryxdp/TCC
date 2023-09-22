def retira_pontuacao(texto):
    Texto = texto
    novo_texto = ''
    i = 0
    while i < len(texto):
        if Texto[i] in '.,!?-:;':
            novo_texto += Texto[:i]+' '
            Texto = texto[i+1:]
        i += 1
    return novo_texto