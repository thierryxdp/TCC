def reticencias():
    return "." *3

def ponto_final():
    return "."

def conta_frases(frases):
    if str.count(frases, ".")>0:
        return str.count(frases, "." and "!" and "?" and reticencias, 0, len(frases))
    
    if str.count(frases, "?"):
        return str.count(frases, "?")
    
    if str.count(frases, "..."):
        return str.count(frases, "...")
    
    if str.count(frases, '!'):
        return str.count(frases