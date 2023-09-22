def conta_frases(texto):
    """A função recebe um texto e devolve o numero de frases que o texto possui. Uma oração só é contada
    como frase se terminar em um desses caracteres: Ponto final, Interrogação, Exclamação ou reticencias. 
    Portanto, a função substitui todos os pontos por ponto final, assim, a premisa vira que 'toda frase termina
    em ponto final'. Com isso, da para separar a o texto em uma lista com várias substrings de cada frase e, então,
    a função ultiliza de 'len' para calcular o numero de indices da lista, ou seja, o numero de frases.;
    str -> int"""
    a = str.replace(texto, '!', '.')
    b = str.replace(a, '?', '.')
    c = str.replace(b,'...','.')
    lista1 = str.split(c, '.')
    return len(lista1)-1