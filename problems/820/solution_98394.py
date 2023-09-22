def posLetra(frase, letra, n):
    ""
    inicio = frase.find(letra)
    while inicio >= 0 and n > 1:
        inicio = frase.find(letra, inicio + 1)
        n -= 1
    return inicio