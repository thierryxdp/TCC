def posLetra(palavra,letra, n):
    pos = palavra.find(letra)
    while pos >= 0 and n > 1:
        pos = texto.find(letra, pos + 1)
        n -= 1
    return pos