def uppCons(frase):
    """Função que retorna as consoantes em maiúscula de uma frase
    str -> str"""
    indice = 0
    parametro = 'bcdfghjklmnpqrstvxyz'
    while indice < len(frase):
        if frase[indice] in parametro:
            maiuscula = str.replace(frase, frase[indice], str.upper(frase[indice]))
        indice += 1
    return maiuscula