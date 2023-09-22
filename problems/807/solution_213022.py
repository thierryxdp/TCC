def conta_frases(texto:str) -> int:
    """Função conta quantas frases há no texto considerando !, ?, . e ... como
       delimitadores e que não tem ! ou ? repetidos
       
       Parameters:
       texto: texto a ser analisado
       
       Returns:
       Quantidade de frases na frase
    """
    sep = '!','?','...','.'
    return str.split(texto, sep)