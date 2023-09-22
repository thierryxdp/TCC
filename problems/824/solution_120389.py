def uppCons(frase):
    """def que ao entregar uma frase, retorna a mesma mas com as consoantes em caixa alta. str --> str"""
    contador = 0
    while contador < len(frase):
        if frase[contador] in "bcdçfghjklmnpqrstvwxyz":
            frase = str.replace(frase,frase[contador],str.upper(frase[contador]),1)
        else:
            frase = frase
        contador += 1
    return frase