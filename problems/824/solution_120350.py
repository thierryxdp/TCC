def uppCons(frase):
    """def que ao entregar uma frase, retorna a mesma mas com as consoantes em caixa alta. str --> str"""
    contador = 0
    
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxyz":
            str.replace(frase,frase[contador],str.upper(frase[contador]))
        contador = contador + 1
    return frase