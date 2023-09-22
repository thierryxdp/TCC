def posLetra(frase, letra, vezes):
    y = 0
    x = 0
    while x <len(frase):
        str.count(frase[:x], letra) == vezes:
        x = x + 1
    return len(frase[:x])