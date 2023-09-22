def uppCons(frase):
    """Funcao que retorna a frase com todas as suas consoantes
    maiusculas e resto como estava"""
    i = 0
    frase1 = ""
    while i < len(frase):
        y = frase[i]
        str.lower(y)
        frase1 = frase1 + y
        i += 1
    return frase1