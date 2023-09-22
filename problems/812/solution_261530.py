def retira_pontuacao(x):
    "A função retorna a frase inicial mas sem os caracteres de pontuação (trocados por espaço) str -> str"
    
    
    i = 0
    u = ''
    y = ['-',',',':',';','.','!','?']

    while len(x) > i:
        if x[i] not in y:
            u = u + x[i]
        if x[i] in y:
            u = u + ' '
        i = i + 1
    return u