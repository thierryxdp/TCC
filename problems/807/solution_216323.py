def conta_frases(text):
    """Conta o numero de frases existentes entro do texto fornecido;
    str -> int"""
    
    pontoR = len(str.split(text, "..."))
    pontoE = len(str.split(text, "!"))
    pontoI = len(str.split(text, "?"))
    pontoF = len(str.split(text, "."))
    
    soma= pontoF + pontoE + pontoI + pontoR
    
    return soma