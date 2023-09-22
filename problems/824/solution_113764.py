def uppCons(frase):
    """Recebe um frase e retorna a frase porém com todas suas consoantes
    em maísculo;
    str -> str"""
    frase_consoante = ""
    i = 0
    vogais = "AEIOUaeiou"
    while i < len(frase):
        if frase[i].strip() not in vogais:
            frase_consoante += frase[i].upper()
        else:
            frase_consoante += frase[i]
        i += 1
    return frase_consoante