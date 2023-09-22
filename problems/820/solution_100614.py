def posLetra(frase, letra, posicao):
    frase = frase.split('')
    pos = 0 # contador
    indices = []# acumulador
    while pos < len(frase):
        if frase[pos] = letra:
            indices = indices + [pos]
        pos = pos + 1
    return indices[2]