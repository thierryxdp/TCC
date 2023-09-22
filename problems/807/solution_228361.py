def conta_frases(texto):
    
    str.replace(texto,'.','...')
    
    texto1=str.count(texto,'...')
    texto2=str.count(texto,'?')
    texto3=str.count(texto,'!')
    
    return texto1+texto2+texto3