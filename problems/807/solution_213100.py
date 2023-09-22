def conta_frases(frase):
    """Função que conta o número de frase a cada pontuação;str->int"""
    frase = str.replace(frase,"...","!")
    contador = 0
    for i in range(len(frase)):
        if frase[i] == "." or frase[i] == "!" or frase[i] == "?":
            contador = contador + 1
    return contador