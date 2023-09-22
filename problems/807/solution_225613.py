def conta_frases(texto):
    """ Função que recebe um texto qualquer como parâmetro de entrada e 
    retorna a quantidade de frases presentes nesse texto.
    
    Obs: Cada frase no texto é terminada com uma ponto final, um ponto de
    interrogação, um ponto de exclamação ou três pontos em sequência (re-
    ticências).Posto isso, os pontos de exclamação ou interrogação não 
    aparecerão repetidos em sequência no texto e tais símbolos só aparecem
    no texto terminando uma frase.
    
    Entrada: str
    Saída: int
    """
    
    t = str(texto)
    
    if '...' in t:
        t = str.replace(t, '...' , '.')
        quant_1 = str.count(t, '.')
        
    if '!' in t:
         t = str.replace(t, '!', '.')
        quant_2 = str.count(t, '.')
    
    if '?' in t:
         t = str.replace(t, '?', '.')
        quant_3 = str.count(t, '.')
    
     
    
    quant_frases = quant_1 + quant_2 + quant_3
    
    return quant_frases