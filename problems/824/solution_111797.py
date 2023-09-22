def uppCons(frase):
    """Função que recebe uma frase e retorna com todas as consoantes em maiusculo.
    parametros:str->str"""
    caracteres = 'bcdfghjklmnpqrstvxwyzç'
    maiusculo = frase
    indice = 0
    while indice < len(frase):
        if frase[indice] in caracteres:
            maiusculo = str.replace(maiusculo, frase[indice], str.upper(frase[indice]))
        indice = indice + 1
    return maiusculo