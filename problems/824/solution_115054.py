def uppCons(frase):
    """Funcao que retorna a frase com todas as suas consoantes
    maiusculas e resto como estava"""
    i = 0
    frase1 = ""
    while i < len(frase):
        if frase[i] in "AaÁáÀàEeÉéIiÍíOoÓóUuÚú":
            str.upper(frase[i])
            frase1 = frase1 + frase[i]
            i += 1
        else:
            str.upper(frase[i])
            frase1 = frase1 + frase[i]
            i += 1
    return frase1