def conta_frases(texto):
    
    texto1=str.count(texto,'.')
    texto2=str.count(texto1,'?')
    texto3=str.count(texto2,'!')
    texto4=str.count(texto3,'...')
    
    return texto1+texto2+texto3+texto4