def uppCons(frase):
    """Entra com uma frase qualquer e retorna a frase
    com todas as consoantes em maísculas (e demais caracteres
    como estavam na frase original).
    str->str"""
    frase_upp=str.upper(frase)
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase_upp[i] in 'AEIOUÁÀÃÉÍÓÕÚ':
            letra_min = str.lower(frase_upp[i])
            frase_final = frase_final + letra_min
        else:
            frase_final = frase_final + frase_upp[i]
        i = i + 1
    return frase_final