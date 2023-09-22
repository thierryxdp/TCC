def uppCons(frase):
    """Entra com uma frase qualquer e retorna a frase
    com todas as consoantes em maísculas (e demais caracteres
    como estavam na frase original).
    str->str"""
    i = 0
    frase_final = ''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÁáÀàÃãÉéÍíÓóÕõÚú':
            letra_maisc = str.upper(frase[i])
            frase_final = frase_final + letra_maisc
        else:
            frase_final = frase_final + frase[i]
        i = i + 1
    return frase_final