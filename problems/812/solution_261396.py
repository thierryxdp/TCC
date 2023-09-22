def retira_pontuacao(x):
    "A função retorna a frase inicial mas sem os caracteres de pontuação (trocados por espaço) str -> str"
    
    i = 0
    u = x
    y = ['-',',',':',';','.']
    
    while len(y) > i:
        if y[i] in x:
            str.replace(x,y[i]," ")
        i = i + 1
    return x