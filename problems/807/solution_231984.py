def conta_frases(x):
    if '.' or '!' or '?' or '...' in x:
        return str.count (x, '. ', '! ','? ',)