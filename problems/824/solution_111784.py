def uppCons(frase):
    """Função que altera as consoantes para maiusculo.
    parametros: str->str"""
    indice = 0
    maiuscula = frase
    caracteres = 'bcdfghjklmnpqrstvxwyzç'
    while indice < len(frase):
        if frase[indice] in caracteres:
            maiuscula = str.replace(maiuscula, frase[indice], str.upper(frase[indice]))
        indice = indice + 1
    return maiuscula