def conta_frases(texto):
    """Função que dada um texto(t) retorne a quantidade de frases que aparecem no texto.
    string -> int"""
    
    x = str.split(texto,'...')
    x = str.join('*',x)
    x = str.split(x,'?')
    x = str.join('*',x)
    x = str.split(x,'!')
    x = str.join('*',x)
    x = str.split(x,'.')
    x = str.join('*',x)
    return (len(str.split(x,'*')))-1