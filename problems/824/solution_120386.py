def uppCons(frase):
    """def que ao entregar uma frase, retorna a mesma mas com as consoantes em caixa alta. str --> str"""
    contador = 0
    renew = ''
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxyz":
            renew += str.upper(frase[contador])
        contador += 1
    return renew