def conta_frases (frases):
    """Dado um texto armazenado em uma string, função que conta o número de frases que aparecem neste texto.
    Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos em sequência (reticências). 
    Pontos de exclamação ou de interrogação não aparecerão repetidos em sequência no texto e esses símbolos só aparecem no texto terminando uma frase. 
    
    entrada ->str
    retorna -> int"""
    
   
    frase2=str.strip (frases,'..')
    sep_fras1=str.count (frase2,'.')
    sep_fras2=str.count (frase2,'!')
    sep_fras3=str.count (frase2,'?')
    
    
    
    return sep_fras1+ sep_fras2+ sep_fras3