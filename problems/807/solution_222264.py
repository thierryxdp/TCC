def conta_frases(frase):
    """funcao que recebe um texto e retorna o numero de frases que esse texto tem, onde cada frase é terminada por um ponto final, exclamação, interrogação ou reticências
	str -> int"""
    
    ponto = str.count(frase, '.', 0)
    exclamacao = str.count(frase, '!', 0)
    interrogacao = str.count(frase, '?', 0)
    trespontos = str.count(frase, '...', 0) * -2 
    
    return ponto + exclamacao + interrogacao + trespontos