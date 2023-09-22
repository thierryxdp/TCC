def uppCons(frase):
    """Função que recebe uma frase e retorna ela com
    as consoantes em maiusculo"""
    i = 0
    while i > len(frase):
        r = ""
        letra = frase[i]
        if letra not in "AEIOUaeiou":
            r = r + str.upper(letra)
            i = i+1
        if letra in "AEIOUaeiou":
            r = r + str(letra)
            i = i+1
    return r