def posLetra(frase, letra, n):
    quant_letras = str.count(frase, letra)
    
    if quant_letras < n:
        return -1
    
    i = 0
    p = 0
    while i < len(frase):
        if frase[1] == letra:
            p += 1
        if p == n:
            return i
        i += 1
    return p