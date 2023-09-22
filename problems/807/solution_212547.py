def reticencias():
    return '.' *3

def pontofinal():
    return '.'

def conta_frases(frases):
    if str.count(frases, '.')>0:
        return str.count(frases, '.' or ':' or '!' or '?' or '...', 0, len(frases))
    
    if str.count(frases, '!')>0 and str.count(frases, '.') == 0:
        return str.count(frases, '!')
  
    if str.count(frases, '?')>0 and str.count(frases, '.') == 0:
        return str.count(frases, '?')
    
    if str.count(frases, '!')>str.count(frases, '.'):
        return str.count(frases, '!' or '.')