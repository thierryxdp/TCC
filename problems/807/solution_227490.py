def conta_frases(texto):
    
    texto1=str.strip(texto,'.')
    texto2=str.strip(texto1,'!')
    texto3=str.strip(texto2,'.')
    texto4=str.strip(texto3,'!')
    
    return len(texto4)