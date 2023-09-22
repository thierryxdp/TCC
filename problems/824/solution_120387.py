def uppCons(frase):
    """def que ao entregar uma frase, retorna a mesma mas com as consoantes em caixa alta. str --> str"""
    contador = 0
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxyz":
            frase += str.upper(frase[contador])
        contador += 1
    return frase