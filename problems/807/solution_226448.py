def conta_frases(texto):
    '''função que retorna o número de frases que aparecem num texto, 
    sendo que cada frase termina por ponto final, de exclamação, de 
    interrogação ou reticências.
    entrada:str
    saída: int'''
    
    texto=str.replace(texto,'!','/')
    texto=str.replace(texto,'.','/')
    texto=str.replace(texto,'?','/')
    texto=str.replace(texto,'...','/')
    
    frases=str.split(texto,'/')
    return len(frases) - 1