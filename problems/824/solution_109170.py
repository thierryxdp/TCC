uppCons(frase):
    """Esta função recebe uma frase e retorne a mesma com todas as suas
    consoantes em maiúsculas e os demais caracteres exatamente como estavam."""
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUãáàéèíóôú':
            frase = frase.replace(frase[i],frase[i].upper())
        i = i+ 1
    return frase