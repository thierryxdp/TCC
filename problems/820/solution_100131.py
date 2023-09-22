def posLetra(frase, letra, vezes):
    y = 0
    x = 0
    while x <= len(frase):
        if str.count(frase[:x], letra) == vezes:
            y = y + len(frase[:x])
        x = x + 1
        
        else:
            -1
    return y