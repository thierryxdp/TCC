def conta_frases (texto):
    """ Função que recebe um texto e conta o número de 
    frases que esse mesmo texto possui.
    tipo de entrada: str
    tipo de saída: int"""
    
    novo_texto = str.replace(texto, "..." , ".")
    
    ponto_final = str.count(novo_texto, "." , 0 , len(texto))
    
    ponto_exclamacao =  str.count(novo_texto, "!" , 0 , len(texto))
    
    ponto_interrogacao = str.count (novo_texto, "?" , 0 , len(texto))
    
    return ponto_final + ponto_exclamacao + ponto_interrogacao