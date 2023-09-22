def posLetra(uma_string, letra, n):
    encontrar = str.find(frase, letra)
    while n > 1:
        if encontrar >= 0:
            encontrar = str.find(frase, letra, encontrencontrar + 1)
        n -= 1
    return encontrar