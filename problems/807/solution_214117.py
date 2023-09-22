def conta_frases(texto):
    
    return texto.count("!")+texto.count("?")+(texto.count(".")-(2*texto.count("...")))