def reticencias():
    return "..."

def ponto_final():
    return "."

def conta_frases(frases):
    if str.count(frases, ponto_final)>0:
        return str.count(frases, ponto_final or "!" or "?" or reticencias, 0, len(frases))
    
    if str.count(frases, "?"):
        return str.count(frases, "?")
    
    if str.count(frases, "..."):
        return str.count(frases, "...")