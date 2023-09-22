def conta_frases(frase):
    
    frase = str.replace(frase,"...","!")
    contador = 0
    for i in range(len(frase)):
        if frase[i] == "." or frase[i] == "!" or frase[i] == "?":
            contador = contador + 1
    return contador