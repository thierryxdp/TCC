def posLetra(frase, letra, n):
    qtd_letras = str.count(frase, letra)
    
    if qtd letras<n:
        return -1
    
    i = 0
    c = 0
    while i < len(frase):
        if frase[1] == letra:
             c += 1
        if c == n:
            return i
        1 += i
    return c