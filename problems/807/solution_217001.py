def conta_frases (texto):
    """ Função que recebe um texto e conta o número de frases que estão no texto.
    tipo de entrada: str
    tipo de saída: int"""
    
    ponto_final = str.count(texto, "." , 0 , len(texto))
    
    ponto_exclamacao =  str.count(texto, "!" , 0 , len(texto))
    
    #reticencias = str.count(texto, "..." , 0 , len(texto))
    
    ponto_interrogacao = str.count (texto, "?" , 0 , len(texto))
    
    return ponto_final +  ponto_exclamacao +   ponto_interrogacao