def posLetra(uma_string, letra, n):
    encontrar = str.find(uma_string, letra)
    while n > 1:
        if encontrar >= 0:
            encontrar = str.find(uma_string, letra, encontrencontrar + 1)
        n -= 1
    return encontrar