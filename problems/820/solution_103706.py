def posLetra(frase, letra, X):
    X = frase[X]
    if letra == frase[X]:
        return X
    else:
        return -1