def conta_frases(texto):
    """..."""
    
    if '...' in frase:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'...') - int(3) + str.count(frase,'.')
    else:
        return str.count(frase,'!') + str.count(frase,'?') + str.count(frase,'.')