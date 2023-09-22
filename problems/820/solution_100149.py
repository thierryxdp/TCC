def posLetra(frase, letra, vezes):
    y = 0
    x = 0
    while x <len(frase):
        if str.count(frase, letra) >= vezes:
            y = y + str.count(frase, letra)
        x= x+1
        return y