def conta_frases(texto:str) -> int:
    """Função conta quantas frases há no texto considerando !, ?, . e ... como
       delimitadores e que não tem ! ou ? repetidos
       
       Parameters:
       texto: texto a ser analisado
       
       Returns:
       Quantidade de frases na frase
    """
    if '!' in texto:
        return exclamacao = texto.count('!')
    elif '?' in texto:
        return interrogacao = texto.count('?')
    elif '...' in texto:
        return reticencias = texto.count('...')
    elif '.' in texto:
        return ponto = texto.count('.')

    return exclamacao + interrogacao + reticencias + ponto