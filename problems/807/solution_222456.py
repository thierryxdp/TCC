def conta_frases(texto):
    ''' Função que conta o número de frases pelas pontuações do texto
    String -> int'''
    texto = str.replace(texto,"?",".")
    texto = str.replace(texto,"!",".")
    texto = str.replace(texto,"...",".")
    
    numeroFrases = str.count(texto,".")
    
    return numeroFrases