def conta_frases(texto):
    
    texto0=str.replace(texto,'...','.')
    
    texto1=str.count(texto0,'.')
    texto2=str.count(texto0,'?')
    texto3=str.count(texto0,'!')
    
    return texto0