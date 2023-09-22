def conta_frases(texto:str) -> int:
    """Função conta quantas frases há no texto considerando !, ?, . e ... como
       delimitadores e que não tem ! ou ? repetidos
       
       Parameters:
       texto: texto a ser analisado
       
       Returns:
       Quantidade de frases na frase
    """
    if '!' in texto:
        return print(exclamacao = texto.count('!'))
    elif '?' in texto:
        return print(interrogacao = texto.count('?'))
    elif '...' in texto:
        return print(reticencias = texto.count('...'))
    elif '.' in texto:
        return print(ponto = texto.count('.'))

    return exclamacao + interrogacao + reticencias + ponto