def conta_frases(texto):
    
    str.replace(texto,'.','...')
    
    texto1=str.count(texto,'...')
    texto2=str.count(texto1,'?')
    texto3=str.count(texto2,'!')
    
    return texto1+texto2+texto3