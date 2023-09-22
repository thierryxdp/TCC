def conta_frases(text):
    """Conta o numero de frases existentes entro do texto fornecido;
    str -> int"""
    
    pontoF = len(str.split(text, '.'))-1
    pontoE = len(str.split(text, '!'))-1
    pontoI = len(str.split(text, '?'))-1
    v1 = str.replace(text, "...", ".")
    pontoR = len(str.split(v1, "."))-2
    
    soma= pontoF + pontoE + pontoI + pontoR
    
    return soma