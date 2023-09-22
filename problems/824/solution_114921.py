def uppCons(frase):
    """Funcao que retorna a frase com todas as suas consoantes
    maiusculas e resto como estava"""
    i = 0
    frase1 = ""
    while i < len(frase):
        frase[i] = y
        if y in "AaEeIiOoUu":
            frase1 = frase1 + y
            i += 1
        else:
            str.upper(y)
            frase1 = frase1 + y
            i += 1
    return frase1