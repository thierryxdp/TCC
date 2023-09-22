def conta_frases(texto:str) -> int:
    """Função conta quantas frases há no texto considerando !, ?, . e ... como
       delimitadores e que não tem ! ou ? repetidos
       
       Parameters:
       texto: texto a ser analisado
       
       Returns:
       Quantidade de frases na frase
    """
    texto2 = str.replace(texto, '...', '{')
    texto3 = str.replace(texto2, '.', '}')
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    reticencias = texto2.count('{')
    ponto = texto3.count('}')
   
    return exclamacao + interrogacao + reticencias + ponto