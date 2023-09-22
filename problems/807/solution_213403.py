def conta_frase(texto):
    """funcao que retorna a quantidade de frases em um texto
    str -> int"""

    ponto = texto.count('.')
    excla = texto.count('!')
    interg = texto.count('?')
    reticencias = texto.count('...')
    n = ponto//3

    if reticencias == n:
        ponto = ponto - n*3 
    

    return ponto + excla + interg + reticencias