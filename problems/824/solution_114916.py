def uppCons(frase):
    """Funcao que retorna a frase com todas as suas consoantes
    maiusculas e resto como estava"""
    indice = 0
    frase1 = ""
    while indice < len(frase):
        y = frase[indice]
        if y == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U"
            frase1 = frase1 + y
            indice += 1
        else:
            str.upper(y)
            frase1 = frase1 + y
            indice += 1
    return frase1